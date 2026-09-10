#!/usr/bin/env python3
"""
Build index.html — the deployable Marks First study site.

Reads the chapter and reference markdown from the repository, bundles it into
the single-page app template, and writes index.html at the REPOSITORY ROOT.

It goes at the root deliberately: Vercel serves a repository root as a static
site with no configuration, so there are no rewrites to misfire. An earlier
version wrote to web/index.html and routed to it via a vercel.json rewrite,
which 404'd on the live deployment.

    python3 web/build.py

Run it again after editing any of the markdown notes.
"""
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

TITLE = "Marks First"
TAGLINE = ("A study app for CBSE Class 12 Maths and Physics: all 27 chapters, 332 board "
           "questions with solutions that stay hidden until you ask, and progress counted "
           "in marks.")

# Emoji favicon as an inline SVG data URI — no extra request, no binary asset.
FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Ctext y='.92em' font-size='88'%3E%F0%9F%93%90%3C/text%3E%3C/svg%3E")

# The reset the Artifact host used to inject; a standalone page needs its own.
RESET = """
*,*::before,*::after{box-sizing:border-box}
html{color-scheme:light dark}
body{margin:0}
img,svg,video{max-width:100%}
[hidden]{display:none!important}
"""


def build_data():
    """Regenerate data.json from the markdown, via build_data.py."""
    r = subprocess.run([sys.executable, os.path.join(HERE, "build_data.py")],
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit("build_data.py failed")


def main():
    build_data()

    src = io.open(os.path.join(HERE, "app.src.html"), encoding="utf-8").read()
    data = io.open(os.path.join(HERE, "data.json"), encoding="utf-8").read()

    # normalise the renderer's sentinels to escape sequences
    src = src.replace('"\u0001"', '"\\u0001"').replace('"\u0002"', '"\\u0002"')
    if any(ord(c) < 9 for c in src):
        raise SystemExit("stray control characters in app.src.html")

    if "/*__DATA__*/" not in src:
        raise SystemExit("data placeholder missing from app.src.html")
    body = src.replace("/*__DATA__*/", data)

    # the template opens with its own <title>; the standalone head supplies one
    body = re.sub(r"^<title>.*?</title>\s*", "", body, count=1, flags=re.S)

    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} &middot; CBSE Class 12 Maths &amp; Physics</title>
<meta name="description" content="{TAGLINE}">
<meta name="theme-color" content="#F6F7FA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F141E" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{FAVICON}">
<link rel="apple-touch-icon" href="{FAVICON}">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE} &middot; CBSE Class 12 Maths &amp; Physics">
<meta property="og:description" content="{TAGLINE}">
<meta name="twitter:card" content="summary">
<style>{RESET}</style>
</head>
<body>
"""
    out = head + body + "\n</body>\n</html>\n"

    dest = os.path.join(ROOT, "index.html")
    io.open(dest, "w", encoding="utf-8").write(out)

    d = json.loads(data)
    qs = sum(len(re.findall(r"^\*\*Q\d+\.\*\*", c["s"]["pyq"], re.M)) for c in d["chapters"])
    size = len(out.encode("utf-8")) / 1048576
    print(f"wrote index.html (repository root)  {size:.2f} MB")
    print(f"  chapters {len(d['chapters'])}  reference docs {len(d['docs'])}  "
          f"board questions {qs}")

    # fail loudly on the things that would silently break the deployed page
    assert "/*__DATA__*/" not in out
    assert out.count("<script") == out.count("</script>")
    hosts = {h for h in re.findall(r"https?://([a-z0-9.-]+)", out)}
    allowed = {"fonts.googleapis.com", "fonts.gstatic.com", "github.com",
               "www.w3.org", "claude.ai", "cbseacademic.nic.in",
               # the "learn it elsewhere" links in each chapter's plain-English intro
               "ncert.nic.in", "www.khanacademy.org", "www.youtube.com"}
    stray = sorted(hosts - allowed)
    if stray:
        print("  note: external hosts referenced:", stray)
    print("  checks passed")


if __name__ == "__main__":
    main()

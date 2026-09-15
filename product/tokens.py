"""The design tokens, in one place because two pages share them.

The palette comes from the thing being sold. A CBSE script is marked in steps
against a marking scheme and totalled in the margin in red, so:

* paper is the cool grey-green of an Indian examination form, not cream;
* one deep institutional teal carries every action;
* red is spent only on marks still at risk — the examiner's pen, not decoration;
* green means marks in hand.

Type has three jobs. Faustina (serif) carries headings, because a printed
question paper is set in a serif. Archivo (grotesque) carries running text and
holds up small. DM Mono carries every number that is a mark, because marks
line up in a margin and want tabular figures.
"""

TOKENS = """
:root{
  --paper:#F1F4F1; --card:#FFFFFF; --sunk:#E7ECE7;
  --ink:#141A1B; --body:#374344; --muted:#5E6D6D; --faint:#8B9898;
  --line:#D4DCD6; --hair:#E3E9E4;
  --accent:#0D4B48; --accent-ink:#0D4B48; --accent-soft:#E2EDEB;
  /* text on a filled accent or semantic ground — a literal #fff would be
     unreadable once the accent lightens for dark mode */
  --on-accent:#FFFFFF; --on-solid:#FFFFFF;
  --mark:#B03127; --mark-soft:#F7E6E3;
  --secured:#2C6742; --secured-soft:#E3EEE6;
  --ochre:#87620F; --ochre-soft:#F6EEDC;
  --shadow:0 1px 2px rgba(20,26,27,.05), 0 6px 20px rgba(20,26,27,.05);
  --lift:0 2px 6px rgba(20,26,27,.08), 0 16px 40px rgba(20,26,27,.09);
  --serif:'Faustina','Noto Serif Devanagari',Georgia,serif;
  --sans:'Archivo','Noto Sans Devanagari',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono:'DM Mono','DejaVu Sans Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  --margin:250px;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#0D1211; --card:#151C1B; --sunk:#1B2322;
    --ink:#E8EEEB; --body:#C3CDC9; --muted:#8B9997; --faint:#667573;
    --line:#28332F; --hair:#202A28;
    --accent:#54B8AC; --accent-ink:#68C6BA; --accent-soft:#0F2A28;
    --on-accent:#06211F; --on-solid:#06211F;
    --mark:#E8796B; --mark-soft:#2C1614;
    --secured:#68C189; --secured-soft:#12251A;
    --ochre:#D3A648; --ochre-soft:#261D0C;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 6px 20px rgba(0,0,0,.3);
    --lift:0 2px 6px rgba(0,0,0,.5), 0 16px 40px rgba(0,0,0,.4);
  }
}
:root[data-theme="dark"]{
  --paper:#0D1211; --card:#151C1B; --sunk:#1B2322;
  --ink:#E8EEEB; --body:#C3CDC9; --muted:#8B9997; --faint:#667573;
  --line:#28332F; --hair:#202A28;
  --accent:#54B8AC; --accent-ink:#68C6BA; --accent-soft:#0F2A28;
  --on-accent:#06211F; --on-solid:#06211F;
  --mark:#E8796B; --mark-soft:#2C1614;
  --secured:#68C189; --secured-soft:#12251A;
  --ochre:#D3A648; --ochre-soft:#261D0C;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 6px 20px rgba(0,0,0,.3);
  --lift:0 2px 6px rgba(0,0,0,.5), 0 16px 40px rgba(0,0,0,.4);
}
"""

FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Faustina:ital,wght@0,400..700;1,400..600"
    "&family=Archivo:wght@400;500;600;700"
    "&family=DM+Mono:wght@300;400;500"
    "&family=Noto+Serif+Devanagari:wght@400;600;700"
    "&family=Noto+Sans+Devanagari:wght@400;500;600&display=swap"
)

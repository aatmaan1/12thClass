"""Selling access to a content product, without shipping it to everyone.

`reskin/` builds tools and `storefront/` takes the money. This is the piece
between them for a product that is *content* rather than a calculator: it
divides the content into a free half and a paid half, signs licence keys for
what a buyer bought, and hands the paid half over one verified key at a time.

The division is the whole design:

* **The free half is compiled into the public page.** It has to be genuinely
  useful on its own, because it is the only part of the offer that is evidence
  rather than copy.
* **The paid half is never in that file.** Not encoded, not hidden behind a
  class — absent. `render.leak_check` refuses the build if it is there.
* **A licence key is signed, not stored.** It verifies with the secret alone,
  so the endpoint stays cheap; a revocation list, checked on every unlock, is
  what lets a refund take access back.

What none of it can do is stop a buyer copying what they paid for. Once
unlocked, the content is in their browser. A paywall stops casual
free-riding, and that is the claim made here.
"""

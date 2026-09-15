"""Funnel and storefront: turning a built product into money.

One architectural decision shapes everything here. **We do not build a
checkout.** Taking card details ourselves would mean becoming the merchant of
record, which for an India-based seller with global buyers means registering
for and remitting VAT/GST across dozens of jurisdictions — the exact risk
notes/build-plan.md flagged. A merchant-of-record provider absorbs all of it
for roughly 5% + 50c.

So the division is:

* **The provider owns** the card form, tax, invoices, refunds and chargebacks.
* **We own** the offer page before it, the delivery page after it, the shape
  of the ladder, and the arithmetic that says whether the ladder is worth
  building at all.
"""

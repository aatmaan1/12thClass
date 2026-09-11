"""Make the product's library importable the way the deployed functions do.

`api/unlock.py` puts `api/_lib` on `sys.path` and imports `paywall.serverless`
flat. The tests import the same modules from `product/` the same way, so what
is tested here is laid out exactly like what runs there — rather than passing
under one import scheme and shipping under another.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "product"))

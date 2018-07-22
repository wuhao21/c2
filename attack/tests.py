# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import re
key = "ad!!!!----!!!]][]{{}{}{safa,.,../.,,,,,'''''''"
key = re.sub(r'[^a-zA-Z0-9\-\,\.\;\?\!\(\)]', '', key)
print(key)
# Create your tests here.

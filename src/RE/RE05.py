# 数量词

import re

_str = 'python Java    ++++**&  &^^%%$$##sctipt C 99981\r171999PHP'

r = re.findall('[a-z|A-Z]+', _str)

print(r)
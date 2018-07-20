import re

_str = 'abc, acc, afc, acr, aft, abb, atf, ain, acf, afc'

r = re.findall('a[c-f]c', _str)

print(r)
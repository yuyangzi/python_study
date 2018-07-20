import re

_str = 'abcpythonJava    ++++**&  &^^%%$$##sctiptC99981\r171999P___HP'

r = re.findall('\s', _str)

print(r)
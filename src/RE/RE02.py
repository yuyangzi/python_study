import re

_str = 'C0C++4JAVA2Python9JavaScript1PHP76Go10'

r = re.findall('\D', _str)
print(r)
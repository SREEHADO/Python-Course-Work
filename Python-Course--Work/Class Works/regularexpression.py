# Regular expression is used for pattern matching in strings. Below is a simple example of how to use regular expressions in Python using the `re` module.
 #Match is used to find a pattern at the beginning of the string.
import re

pattern = r'hello'
res= re.match(pattern, 'hello world')

print("Matched" if res else "Not Matched")

import re

pattern = r'[0-9]'
res= re.match(pattern, '12 hello world')

print(res.group() if res else "Not Matched")

#Search is used to find a pattern anywhere and entire in the string.
import re

pattern = r'[aeiou]'
res= re.search(pattern, '12 hello world')

print(res.group() if res else "Not Matched")


import re

pattern = r'[0-9]'
res= re.findall(pattern, 'hello12 9 6 5 3 8 7 66 world')

# print(res.group() if res else "Not Matched")
print(res)


import re

pattern = r'[0-9]'
res= re.finditer(pattern, 'hello12 9 6 5 3 8 7 66 world')

for i in res:
    print(i.group(), i.start())


import re

pattern = r'[,.>:;]'
res= re.split(pattern, 'hello, world. welcome: to; python> programming')

print(res)

# for i in res:
   # print(i.group(), i.start())


import re

pattern = r'123'
res= re.sub(pattern, '*', 'hello123 world123, welcome to python123 programming123')

print(res)

























































































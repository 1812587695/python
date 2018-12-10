import re

a = 'xy123'
b = re.findall('x...', a)
print(b)
b = re.findall('x*', a)
print(b)

b = re.findall('y(.*)2', a)
print(b)
for e in b:
    print(e)
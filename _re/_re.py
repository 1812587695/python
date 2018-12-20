import re

print(re.match('www', 'www.runoob.com').span())

print(re.match('com', 'www.runoob.com'))

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) Are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))




print('--------------------------------------------')
print(re.match('abc','abcefg'))
print(re.match('abc','abcefg').group())  #匹配开头，group方法返回分组字符串。

r1 = re.match('abc','1abcefg')
print(r1)   #开头未匹配到返回none

print('--------------------------------------------')
pattern = re.search('w','aw,bw,cw,dw')  #匹配结果
print(pattern)
print(pattern.group())
print(pattern.start())
print(pattern.end())
print('--------------------------------------------')
print(re.search(r'(r[au]n)', "dog runs to cat").group(1))
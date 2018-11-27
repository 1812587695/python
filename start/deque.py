from collections import deque

d=deque()

d.append(3)

d.append(8)

d.append(1)

print(d)

d=deque('12345')
print(d)
d.pop()
print(d)
d.extend([0])
print(d)

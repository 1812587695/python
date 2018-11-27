
#s生成器表达式
old_gen = (i for i in range(21) if i % 2 == 1)
print(type(old_gen))
for item in old_gen:
    print(item)

print(type(old_gen))


a = list(old_gen)
print(type(a))
print(a)


# 自定推导式
my_dict = {"a" : 1, "b" : 2, "c" : 3}
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)
class Student(object):
    def __getattr__(self, item):
        return item + ' is not exits'

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


s = Student()
print(s.name)  # 调用__getattr__方法 输出'name is not exits'
s.age = 1  # 调用__setattr__ 方法
print(s.age)  # 输出 1
print(s['age'])  # 调用 __getitem__方法 输出1
s['name'] = 'tom'  # 调用 __setitem__ 方法
print(s['name'])  # 调用 __getitem__ 方法 输出 'tom'



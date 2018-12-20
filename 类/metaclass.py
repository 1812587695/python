# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # attrs['add'] = lambda self, value: self.append(value)
        # print(name)
        # print(bases)
        if name == 'MyList':
            return type.__new__(cls, name, bases, attrs)

        print(attrs)
        # for k,v in attrs.items():
        #     print(k, v)

        mappings = dict()
        # print(attrs)
        for k, v in attrs.items():
            if k != '__module__' and k != '__qualname__':
                mappings[k] = v


        attrs['__vvv__'] = mappings
        # print(attrs)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(dict, metaclass=ListMetaclass):
    # def __init__(self, **kwargs):
    #     for name, value in kwargs.items():
    #         setattr(self, name, value)
    #         print('=======', name, value)


    # def __getattr__(self, key):
    #     try:
    #         print(self[key])
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    #
    # def __setattr__(self, key, value):
    #     print(self[key])
    #     self[key] = value

    def aa(self):
        print(self)
        for k, v in self.items():
            print('---', k, v)
        # print(self.__vvv__)


# 当我们传入关键字参数metaclass时，魔术就生效了，
# 它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，
# 比如，加上新的方法，然后，
# 返回修改后的定义

# l = MyList()
# l.add(1)
# print(l)

class T(MyList):
    a = 'a'
    b = 'b'
    c = 'c'



t = T(a=1, b=2, c='a')

t.aa()

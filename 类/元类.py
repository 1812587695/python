class Meta(type):
    def __new__(meta, *args, **kwargs):

        clsname, bases, namespace = args

        print(clsname, 'class created')
        return super().__new__(meta, *args)

    def __init__(cls, *args, **kwargs):
        print(cls.__name__, 'class inited')
        super().__init__(*args)


class Base(metaclass=Meta):
    a = 1
    b = 2

    print('class defined')

    def __new__(cls, *args, **kwargs):
        print(cls.__name__, 'class instance created')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(type(self).__name__, 'class instance inited')


    def hello(self):
        pass


# b = Base()
# print(type(Base))
#
# print("*" * 90)

# b = Base()
# print(type(Base))
# print("*" * 90)
# print(b)

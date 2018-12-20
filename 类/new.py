class Singleton:
    instance = None

    def __new__(cls, xx, yy):

        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy


obj1 = Singleton(22, 33)

obj2 = Singleton(44, 55)

print(obj1.xx, obj2.xx)
print(obj1 is obj2)
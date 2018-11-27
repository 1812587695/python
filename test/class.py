class StaticMethodExample():
    staticval = 1

    def __init__(self):
        print(self.staticval)
        print(self.__class__)

    # 标注为静态方法
    @staticmethod
    def plus(x, y):
        StaticMethodExample.staticval += 1
        print("x+y=" + str(x + y))


StaticMethodExample.plus(1, 2)

StaticMethodExample()
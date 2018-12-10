class Parent:
    def __init__(self):
        # 父类的构造函数
        print("父类构造完毕")


class Child1(Parent):
    # child1类继承于 parent类
    def __init__(self):
        super().__init__()
        print("子类1代构造函数")


class Child2(Child1):
    # child2类继承于 child1类
    def __init__(self):
        super().__init__()
        print("子类2代构造函数")


def main():
    # 构造函数有了super()才能追本溯源呀，但是。。。Child1没有super
    Child2()


if __name__ == '__main__':
    main()
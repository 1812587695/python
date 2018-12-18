from abc import ABC, abstractmethod

'''
抽象方法是父类的一个方法, 
父类没有实现这个方法, 父类是不可以实例化的.
子类继承父类, 子类必须实现父类定义的抽象方法, 子类才可以被实例化.
Python中的abc提供了@abstractmethod装饰器实现抽象方法的定义
'''
class Foo(ABC):
    @abstractmethod
    def fun(self):
        """
        你需要在子类中实现该方法, 子类才允许被实例化
        """


class SubFoo(Foo):

    def fun(self):
        print("子类实现父类的抽象方法")


if __name__ == "__main__":

    sf = SubFoo()
    sf.fun()
class Money(object):
    def __init__(self):
        self.__money = 0

    '''
       @property 将方法变成属性，让get和set方法更好用
       看上去的确好用,但其实python内置的__getattr__和__setattr__就是将方法变为属性功能的
    '''
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")


a = Money()
# 获取对象中的money属性值，当前结果为0
print(a.money)

a.money = 100
# 获取对象中的money属性值，当前结果为100
print(a.money)
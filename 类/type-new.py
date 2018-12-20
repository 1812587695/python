class User(type):

    def __new__(cls, name, bases, attrs):
        print("new")
        # cls.name = name + "bb"
        # print(type.__new__)
        # print(super().__new__)
        return type.__new__(cls, name, bases, attrs)

    # def __init__(self, name):
    #     self.name = name + "aa"
    #     print("init")


# user = User()
class T(object, metaclass=User):
    def aa(self):
        print("aa")


u = T()
# print(u.name)
print(type(u))

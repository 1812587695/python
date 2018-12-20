class User:
    def __new__(cls, name):
        print("new")
        cls.name = name + "bb"
        print(type.__new__)
        print(super().__new__)
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name + "aa"
        print("init")


# user = User()

u = User("body")
print(u.name)
print(type(u))

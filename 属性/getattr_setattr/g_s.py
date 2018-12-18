class Stu(object):
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self):
        return self.name


s = Stu()
s.名称 = 'alex'
print(s.名称)

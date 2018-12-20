
class A(object):
    def aa(self):
        print(self)


class B(A):
    def __init__(self, **kw):
        super(B, self).__init__(**kw)
    pass

b = B(a = 'a')
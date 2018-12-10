from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances

    return getinstance


@singleton
class Bar:
    pass


b0 = Bar()
b1 = Bar()
print(id(b0))
print(id(b1))
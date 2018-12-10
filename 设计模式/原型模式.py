import copy

class ProtoType(object):
    def __init__(self):
        super().__init__()
        self.setting_a = "a"
        self.setting_b = "b"


    def clone(self, **kwargs):

        obj = copy.deepcopy(self)
        obj.__dict__.update(**kwargs)
        return obj


def main():
    prototype = ProtoType()
    prototype_diff = prototype.clone(setting_a="x", setting_b="y")
    print(prototype_diff.setting_a, prototype_diff.setting_b)
    print("id_prototype", id(prototype), "id_prototype_diff", id(prototype_diff))


if __name__ == '__main__':
    main()
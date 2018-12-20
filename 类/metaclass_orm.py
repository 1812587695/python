class CharField:
    def __init__(self, db_column, max_length=None):
        self.db_column = db_column
        self.max_length = max_length
        if max_length is not None:
            if not isinstance(max_length, int):
                print("最大值要是int类型")
            elif max_length < 0:
                print("不能小于0")

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str) and len(value) < self.max_length:
            self.value = value
        else:
            print("字符串的长度不能大于最大值  和必须是string 类型")


class IntField:
    def __init__(self, db_column, max=None, min=None):
        self.min_length = min
        self.db_column = db_column
        self.max_length = max
        if max is not None:
            if not isinstance(max, int):
                print("最大值要是int类型")
            elif max < 0:
                print("不能小于0")
        if min is not None:
            if not isinstance(max, int):
                print("最大值要是int类型")
            elif max < 0:
                print("不能小于0")
        if max is not None and min is not None:
            if min > max:
                print("最大值怎么可能大于最小值呢")

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int) and self.min_length < value < self.max_length:
            self.value = value
        else:
            print("请检查年龄是否合法")




class User:
    name = CharField(db_column="", max_length=10)
    # 定义表的列 name 字段，db_columns是表列名称，并用max_length 校验字段的长度
    age = IntField(db_column="", min=0, max=100)

    # 定义表的列 name 字段，db_columns是表列名称，并用max_length and min_length 校验字段的长度

    class Meta:
        db_table = ""
    # 添加Meta class 有两个目的 ，1.添加表名称 2.和表的列分开，这样思路比较清晰


user = User()

user.name = "Andy"
user.age = 10
print(user.name, user.age)  # Andy 10

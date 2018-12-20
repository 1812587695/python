# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s> 11111111' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 类的模板定义  ModelMetaclass
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):

        # 排除掉对Model类的修改,Model类中有metaclass是具体数据表类的父类,不能自己实现只提供继承
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # print('Found model: %s' % name)
        # 保存Field 属性到mappings中
        # print("----------------", dict())
        mappings = dict()
        # print(attrs)
        for k, v in attrs.items():
            # print(k, v)
            if isinstance(v, Field):
                # print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删除attrs中Field属性，防止运行时，实例的属性遮盖类的同名属性出现异常
        # print('---------------', mappings)
        for k in mappings.keys():
            attrs.pop(k)
        # 保存属性和列的映射关系
        # print('================', mappings)
        attrs['__mappings__'] = mappings
        # 假设表名和类名一致
        attrs['__table__'] = name
        # print('****************')
        # print(name)
        # print(bases)
        # print(attrs)
        return type.__new__(cls, name, bases, attrs)


# 创建具体数据表的基类
class Model(dict, metaclass=ModelMetaclass):

    # def __init__(self, **kw):
    #     super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 定义一个操作数据库的方法
    def save(self):
        fields = []
        params = []
        args = []
        # print(self.__mappings__)
        # print(self)
        for k, v in self.__mappings__.items():
            # print(getattr(self, k, None))
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        # 拼接sql语句
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 定义一个具体的数据表类，继承Model
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

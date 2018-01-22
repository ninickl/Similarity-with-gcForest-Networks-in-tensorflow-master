class Person(object):
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):   # 这里相当于默认的getter属性
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    @name.deleter
    def name(self):
        del self.__name

p1=Person("panpan")
print(p1.name)  # 这里是 p1.name 而不是 p1.__name 是因为装饰器name可以当做属性访问类的私有成员
p1.name="zhenzhen"
print(p1.name)
print(p1.__dict__,p1.__class__,p1.__doc__)
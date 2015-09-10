__author__ = 'bruno'

class MyClass(object):
    def __init__(self):
        print("init")

    def f(self):
        print("f")

x = MyClass()
print(x.f)

print(MyClass.f)

# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo, self.bar)
        print(self.name)

c = C()
c.showprops()
print(C.__mro__)
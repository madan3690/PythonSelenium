class A:
    def m1(self):
        print(1)

class B(A):
    def m2(self):
        print(2)
        super().m1()

b=B()
b.m2()
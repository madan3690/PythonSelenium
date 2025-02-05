class A:
    def m1(self):
        print(1)

class B:
    def m1(self):
        print(2)

class C(B,A):
    def m3(self):
        print(3)
        super().m1()

co=C()
co.m3()
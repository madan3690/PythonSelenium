def do(func,x,y):
    z=func(x,y)
    print(z)


def add(x,y):
    return x+y
def mul(x,y):
    return x*y

do(add,1,2)
do(mul,6,8)

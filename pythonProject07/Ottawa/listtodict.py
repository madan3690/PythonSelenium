def listtodict(l1,l2):
    return dict(zip(l1,l2))

def listtoset(l1):
    return set(l1)

def listtotuple(l1):
    return tuple(l1)

a=[1,2,3]
b=[4,5,6]
c=[1,4,5,6,3,2,1,4,5]

print(listtodict(a,b))
print(listtoset(c))
print(listtotuple(c))
# print(listtotuple(listtodict(a,b)))

"""print("back")"""
import keyword

print(keyword.kwlist )

x=700
print(x)
print(type(x))
x='mafia'
print(x)
# dynamically typed
print(type(x))
a=(0,0)
print(type(a))
a={0,0}
print(type(a))
 # dynamically typed

b=True
print(type(b))


q,w,e=10,9,'madan'
print(q,w,e)

t=y=u=700

print(t,y,u)

g=8
h=9
print(g,h)
g,h=h,g
print(g,h)

del g
print(g)
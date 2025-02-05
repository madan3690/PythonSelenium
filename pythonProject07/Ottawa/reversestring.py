abc = "Welcome to python programming"
# print(abc[::-1])
q=""
s=abc.split()
for a in s:
    a=a[::-1]
    q=q+a+" "

print(q)
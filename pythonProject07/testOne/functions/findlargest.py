def large(a,b,c):
    if a>b:
        x=a
    else:
        x=b

    if x>c:
        return x
    else:
        return c

print(large(1000,2000, 300))
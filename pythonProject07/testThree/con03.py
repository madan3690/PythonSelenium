class Cons:
    def __init__(self,a,b):
       self.a=a
       self.b=b

    def __str__(self):
        return(self.a)


c=Cons('4','5')
print(c)
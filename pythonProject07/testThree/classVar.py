class Newr:
    a,b=40,50


    def add(self):
        #a,b=90,70
        print(self.a,self.b)
        print(a,b)
        print(globals()['a'],globals()['b'])

a,b=10,20
n1=Newr()
#n1.add()
Newr().add()

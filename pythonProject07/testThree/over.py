class Human:
    def sayhello(self,name=None):
        if name is not None:
            print('Hello '+str(name))
        else:
            print('Hello Stranger')

    def sayhello(self,x=0,y=0,z=0):
        print('numbers'+str(x))

h=Human()
h.sayhello()
h.sayhello('4')
h.sayhello(7)
h.sayhello('madan')
h.sayhello('007')
h.sayhello(9)
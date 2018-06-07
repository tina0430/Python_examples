class Nice :
    name=''
    mynum1=id(name)
    mynum2=0
    mynum3=2
    
    def __init__ (self, name):
        self.name = name
        self.mynum2 = id(self.name)
        self.mynum3 = id(name)
        
    def myPrint (self):
        print(self.mynum1, id(self.mynum1))
        print(self.mynum2, id(self.mynum2))
        print(self.mynum3, id(self.mynum3))
        
n = Nice('jihee')
n.myPrint()
from abc import ABCMeta, abstractmethod

class Friend(metaclass =ABCMeta):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def hobby(self):
        pass
    
    def printName(self):
        print('이름은 '+self.name)
        
class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self):
        print('John의 취미 : '+ self.addr+'거리를 걸어다님')
    
    def printAdd(self):
        print('John의 주소 : '+ self.addr)

class Chris(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
    
    def hobby(self):
        print('Chris의 취미 : '+ self.addr+'동네를 뛰어다님')
        print(self.addr+'에 살고 있다.')
        
john = John('john', 'Ocha St, 94451')
john.printName()
john.printAdd()
john.hobby()

print()
chris = Chris('chris', 'Saratoga Ave, 94231')
chris.printName()
chris.hobby()
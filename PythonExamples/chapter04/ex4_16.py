a = 10
b = 5

print(a+b, a-b)

class AddClass:
    def __init__(self, s):
        self.s = s
        
    def __add__(self, arg):
        return '더하기 결과는 ' + str(self.s + arg)

class StrClass:
    def __init__(self, initData):
        self.str = initData
    
    def __sub__(self, other):
        for i in other:
            self.str = self.str.replace(i,'')
        return StrClass(self.str)
            
    def __abs__(self):
        return StrClass(self.str.upper())
    
    def printData(self):
        print(self.str)
                
ac1 = AddClass('kbs')
print(ac1+'mbc')

ac2 = AddClass('당신의 이름은')
print(ac2+'홍길동')

print('\n======')

sc = StrClass('aBsdEfgHi Korea')
print('sc', sc.str)

print()
sc = sc - 'aB'
sc.printData()
sc -= 'cdi'
sc.printData()

print()
print(abs(5), abs(-5))
sc = abs(sc)
sc.printData()
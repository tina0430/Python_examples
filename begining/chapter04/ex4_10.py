class Parent :
    def printData(self):
        print('나는 부모다!')

class Child1(Parent):
    def printData(self):
        print('Child1에서 override')

class Child2(Parent):
    def printData(self):
        print('Child2에서 overriding')    #부모의 메소드와 이름은 같으나 기능은 다름s

c1 = Child1()
c1.printData()
print()

c2 = Child2()
c2.printData()
print()

par = Parent()
par.printData()
print()

par = c1
par.printData()
print()

par = c2
par.printData()
print()

plist = [c1, c2, par]
for item in plist:
    item.printData()
    print()
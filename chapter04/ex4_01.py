class TestClass :
    aa = 1
    def __init__(self):
        print('생성자 ')
    def __del__(self):
        print('소멸자 ')
        
    def printMessage(self):
        name='한국인'
        print(name)
        print(self.aa)
        
test = TestClass()
test2 = TestClass()
print(test.aa)
print(TestClass.aa)
#print(TestClass.name)    #error

print()
print('메서드 호출하는 법')
test.printMessage()
print(test.printMessage())            #Bound Method call
print(TestClass.printMessage(test))   #Unbound Method call
#print(test2.printMessage(test))      #error
print()
print('클레스 타입 확인:', isinstance(test, TestClass))
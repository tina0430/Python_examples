class Person:
    say = '난 사람이야'
    age=24
    
    def __init__(self, age):
        self.age = age
        
    def printInfo(self):
        print('나이 : {}, 이야기 : {}'.format(self.age, self.say))
    
    def hello(self):
        print('안뇽!')
    
class Employee(Person):
    subject='근로자'
    say = '나는 피고용자'
    
    def __init__(self):
        print('Employee 생성자 호출됨')
        
    def emPrintInfo(self):
        super().printInfo()
        print(self.say, super().say)
        self.hello()    #나중에 유지보수할떄 개빡
        super().hello() #이렇게 해야 괜츈
        
class Worker(Person):
    def __init__(self, age):
        print('Worker 생성자 호출됨')
        super().__init__(age)
        
    def worPrintInfo(self):
        #super().say = '나는 워커(신발 아님)' #error
        print('나이 : {}, 이야기 : {}'.format(super().age, super().say))
    
class Programmer(Worker):
    def __init__(self, age):
        print('Worker 생성자 호출됨')
        #super().__init__(age)    #Bound call - 권장
        Worker.__init__(self, age)#Unbound call
        self.say = '나는 프로그래머'
       
    def worPrintInfo(self):
        print('오버라이딩')

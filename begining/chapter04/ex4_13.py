class Donkey:
    data = '당나귀 최고!'
    
    def skill(self):
        print('당나귀 : 짐나르기')

    def eat(self):
        print('당나귀 당근 얌얌')

class Horse:
    def skill(self):    
        print('말 : 달리기')
        
    def hobby(self):
        print('말은 달리기가 취미')

class Mule1(Donkey, Horse):
    pass

class Mule2(Donkey, Horse):
    #data = '노새 만세'
    
    def play(self):
        print('노새는 총총 논다')
        #data = 'dd'
        print(self.data)
    
    def hobby(self):
        print('노새는 초원 걷기를 즐김')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        hobby()
    
    def showData(self):
        data = '지역변수'
        print(self.data)
        print(super().data)
        print(data)
        
mule1 = Mule1()
print(mule1.data)
mule1.skill()   #다중 상속시 상속 구문에 먼저 명시된 부모의 함수 실행
mule1.eat()
mule1.hobby()

def hobby():
    print('전역 함수의 hobby!')
print('**'*5)
    
mule2 = Mule2()
print(mule2.data)
mule2.skill()
mule2.eat()
mule2.hobby()
mule2.play()


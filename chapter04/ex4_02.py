class Car :
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def getData(self):
        km = '킬로미터'
        msg = '속도 :' + str(self.speed) + km
        return msg
    
print(Car.handle)
    
car1 = Car('tom', 10)
print(car1.handle, car1.name, car1.speed)
car1.color = '검정'
print('car1.color :', car1.color)

print()
car2 = Car('eliot', 20)
print(car2.handle, car2.name, car2.speed)
#print('car2.color :', car2.color)   #error

print('\n주소 출력')
print(Car, car1, car2, sep = '\n')
print(id(Car), id(car1), id(car2), sep = '\n')

print('\n메서드 사용')
print('car1 ', car1.getData())
print('car2 ', car2.getData())
car1.speed = 50
car2.speed = 80
print('car1 ', car1.getData())
print('car2 ', car2.getData())

print('\n각 객체의 speed 확인')
print('car1 속도 :', car1.speed)
print('car2 속도 :', car2.speed)
print('Car Class 속도 :', Car.speed)

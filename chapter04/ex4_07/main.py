from chapter04.ex4_07.robot import Robot

print('메인 시작!')
robot1 = Robot()                  #새로운 Robot인스턴스를 robot이 참조
#robot1.name = '뀨'
print('robot1 이름 :', robot1.name)
print('robot1 에너지 :', robot1.energy)
print('robo1  주특기 :', robot1.attack())  #Bound Method call
print(robot1.__dict__)

print()
robot2 = Robot                   #Robot원형 클래스를 robot2가 참조
print(robot2.__dict__)
robot2.name = '썬가드'             #Robot원형 클래스에 새로운 name 값 입력
print(robot1.__dict__)
print(robot2.__dict__)
print('robot1 이름 :', robot1.name)
print('robot2 이름 :', robot2.name)
print('robot2 에너지 :', robot2.energy)
print('에너지 충전~~~~~~!')
robot2.energy = 80
print('robot2 에너지 :', robot2.energy)
print('robot2 주특기 :', robot2.attack(robot2))    #Unbound Method call
print('Robot  에너지 :', Robot.energy)

print()
print('robot1 이름 :', robot1.name)
print('robot2 이름 :', robot2.name)
print('Robot1 이름 :', Robot.name)

print()
robot1.name='옵티머스 프라임'   #Robot type의 객체의 name값 변경
print('robot1 이름 :', robot1.name)
print('robot2 이름 :', robot2.name)
print('Robot  이름 :', Robot.name)
from ex4_05_01 import Car 

tom = Car('tom')
tom.turnHandle(10)
print(tom.name+'의 회전량은 '+tom.state + str(tom.handle.quantity))

tom.turnHandle(-20)
print(tom.name+'의 회전량은 '+tom.state + str(tom.handle.quantity))

oscar = Car('oscar')
tom.turnHandle(0)
print(oscar.name+'의 회전량은 '+oscar.state + str(oscar.handle.quantity))
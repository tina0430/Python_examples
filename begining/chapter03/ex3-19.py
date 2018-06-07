import turtle
from time import sleep

a = turtle.Pen()
a.speed(6)

a.forward(100)
a.right(90)
a.forward(100)
a.right(90)
a.forward(100)
a.right(90)
a.forward(100)

#a.reset() #화면 초기화

a.pencolor('blue')
a.circle(50, 360)

a.up()
a.forward(100)
a.write('문자그리기', True, 'left', font=('돋움', 24, 'normal'))
sleep(10)
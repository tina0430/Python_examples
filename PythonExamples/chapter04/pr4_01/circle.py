import math

class Circle:

    PI = math.pi    
    def __init__(self, name, xpos, ypos, radius):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
    
    def showInfo(self):
        print(self.name+'에 대한 정보')
        print('원 중심 : {}, {}'.format(self.xpos, self.ypos))
        print('반지름 :%.1f'%(self.radius))
        print('면적 : %.1f\n'%(self.PI*(self.radius**2)))
        
circle1 = Circle('원1', 3, 5, 10)
circle2 = Circle('원2', 8, 6, 20)

circle1.showInfo()
circle2.showInfo()

class Handle :
    quantity = 0
    
    def Turn(self, quantity):
        self.quantity = int(quantity)
        
        if (quantity == 0):
            return '직진'
        elif (quantity < 0):
            return '좌회전'
        else:
            return '우회전'
    
class Car :
    state = '정지'
    def __init__(self, name):
        self.name = name
        self.handle = Handle()
    def turnHandle(self, quantity):
        self.state = self.handle.Turn(quantity)
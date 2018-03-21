from chapter04.ex4_11.elecProduct import ElecProduct

class ElecTV(ElecProduct):
    
    def __init__(self, maxVolume, volt):
        super().__init__(maxVolume, volt)
    
    def turnOn(self):
        if not self.state:
            print('화면이 켜져서 빠라밤~~!')
            self.state = True
        print(super().state)
        print(self.state)
        
    def turnOff(self):
        if self.state:
            print('삐루비룸... 까만 화면 됨!')
            self.state = False
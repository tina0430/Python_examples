from chapter04.ex4_11.elecProduct import ElecProduct

class ElecRadio(ElecProduct):
    
    def __init__(self, maxVolume, volt):
        super().__init__(maxVolume, volt)
    
    def turnOn(self):
        if not self.state:
            print('소리가 켜졌다 뚜루루룩')
            self.state = True
        
    def turnOff(self):
        if self.state:
            print('뚝! 소리 안남!')
            self.state = False
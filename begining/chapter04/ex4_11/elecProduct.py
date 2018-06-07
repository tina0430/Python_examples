class ElecProduct:
    volt = 0
    state = False
    volume = 0
    
    def __init__(self, maxVolume, volt):
        self.maxVolume = maxVolume
        self.volt = volt
        
    def volumeControl(self, volume):
        if 0 < self.volume+volume < self.maxVolume :
            self.volume += volume
            print('소리크기 :', self.volume)
        elif self.volume+volume < 0:
            print('이미 소리가 0')
        else:
            print('이미 너무 커서 더 키울 수 없음 ㅜㅜ')
        
    
    def turnOn(self):
        pass
    
    def turnOff(self):
        pass
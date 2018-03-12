from chapter04.ex4_11.elecRadio import ElecRadio
from chapter04.ex4_11.elecTV import ElecTV

myTV = ElecTV(20, 220)
print(myTV.__dict__)
myTV.turnOn()
myTV.volumeControl(18)
myTV.volumeControl(3)
myTV.turnOff()

myRadio = ElecRadio(30, 110)
myRadio.turnOn()
myRadio.volumeControl(-3)
myRadio.turnOff()
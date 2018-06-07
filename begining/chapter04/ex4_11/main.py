'''
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
'''
from audioop import reverse
student_tuples = [('john', 'A', 15),('jane', 'B', 30),('dave', 'B', 10)]
print(sorted(student_tuples, key=lambda student: student[2]))
print(sorted("This is a test string from Andrew".split(), key=str.lower))
print(sorted("This is a test string from Andrew".split()))
print(sorted("This is a test string from Andrew".split(), reverse = True))

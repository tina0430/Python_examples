from ex4_09_01 import *

print(Person.say, Person.age)
per = Person('22')
per.printInfo()
per.hello()

print('--' * 10)
em = Employee();
em.emPrintInfo()
em.printInfo()

print('--' * 10)
wor = Worker(45)
print(wor.say, wor.age)
wor.worPrintInfo()
wor.printInfo()

print('--' * 10)
pr = Programmer(33)
print(pr.age, pr.say)
pr.worPrintInfo()
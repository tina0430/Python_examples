from chapter04.ex4_06.food import Food
from chapter04.ex4_06.fridge import Fridge

myFridge = Fridge()

apple = Food('사과', '2018-04-05')
myFridge.open()
myFridge.put(apple)
myFridge.close()

apple = Food('배', '2018-04-15')
myFridge.put(apple)

print()
coke = Food('콜라', '2019-02-20')
myFridge.open()
myFridge.put(coke)
myFridge.close()
#카페 1377

list1 = [1,2,3,4]
list2 = [4,5,6]
list3 = [7,8]

new1 = list(zip(list1, list2))
print(new1)

new2 = list(zip(list1, list2, list3))
print(new2)

str1 = 'abc'
str2 = 'def'
new3 = list(zip(str1,str2))
print(new3)


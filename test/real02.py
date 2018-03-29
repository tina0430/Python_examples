# import matplotlib.pyplot as plt
# plt.figure()
# plt.xlabel('x-asix label')
# plt.ylabel('y-asix label')
# plt.plot((0,1,2,3),(1,3,2,4))
# plt.show()

# import pandas as pd
# result=[]
# myColumns = ('이름','나이')
# myEncoding= 'utf-8'
# mydata = [('김철수', 10), ('박영희', 20)]
# sublist =[]
# sublist.append(mydata[0])
# sublist.append(mydata[1])
# result.append(sublist)
# data = pd.DataFrame(result, columns=myColumns)
# data.to_csv('abc.data', columns=myColumns, encoding=myEncoding,header=0,mode='w',)

# <famaily>
#     <dad>
#         <name>홍길동</name>
#         <age>60</age>
#     </dad>
#     
#     <mom>
#         <name>박영희</name>
#         <age>55</age>
#     </mom>
#     
#     <son>
#         <name>홍만길</name>
#         <age>25</age>
#     </son>
#     
#     <daughter>
#         <name>홍진숙</name>
#         <age>25</age>
#     </daughter>
# </family>

# import numpy as np
# print(np.random.randint(1, 6, size=3))

# import numpy as np
# from pandas import Series 

# mydata = [1, -2, 3, -4, 5]
# s = Series(mydata)
# print(np.sum(np.power(np.abs(s),2)))



some_list=['a','d','w','r']
for counter, value in enumerate(some_list):
    print(counter, value)
print('-'*10)
for counter, value in enumerate(some_list, 2):
    print(counter, value)

a = enumerate(some_list, 1)
print(a)
print(list(a))
print(type(a))



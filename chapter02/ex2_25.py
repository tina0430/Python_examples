#2단 3단 출력, 이중 for문 사용

no = 1
for dan in [2,3]:
    print('--%d단--'%dan)
    for no in [1,2,3,4,5,6,7,8,9]:
        print(dan,'*', no)
    print()
    
list1 = [3,4,5]
list2 = [2,3]
no = 0

for i in list1:
    for j in list2:
        print(i*j, end = ' ')
        
print()

datas = [i*j for i in list1 for j in list2]
print(datas)

for d in datas :
    print(d, end = ' ')
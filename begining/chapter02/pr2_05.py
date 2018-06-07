#별 찍기
 
#죄측 정렬
i = 1
h = int(input('트리 높이 선택 :'))
while i < h+1 :
    print('*' * i)
    i += 1
    
print("=" * 20)

#우측 정렬
i = 1
while i < h+1 :
    print(' ' * (h-i), '*' * i, sep='')
    i += 1

#대칭
i = 1
while i < h+1 :
    print(' ' * (h-i), '*' * (2*i-1), sep='')
    i += 1
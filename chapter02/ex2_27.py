for i in range(6) : 
    print(i, end = ' ')
    
print('\n\n1~10의 합:', end = ' ')
total = 0

for i in range(1, 11) :
    total += i
print(total)

print('내장 함수 sum()사용 :', sum(range(1, 11)))

print()
matrix=[[1,2,3], [4,5,6]]
print('matrix[0][0]은',matrix[0][0])
print('matrix의 행의 요소 개수:', len(matrix))
print('matrix의 열의 요소 개수:', len(matrix[0]))

print()
print('matrix값 출력')
for i in range(2) : 
    for j in matrix[i] : 
        print(j, end = ' ')
    print()
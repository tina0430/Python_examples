fd = open('newfile.txt', 'w', encoding='utf-8')

#파일 하나 만들기
for i in range(1, 11) :
    data = '%d번째 줄입니다.\n'
    fd.write(data)
    
fd.close()

#여러개의 바일 만들기
for i in range(1, 11) :
    fd = open('somefile' + str(i) + '.txt', 'w', encoding='utf-8')
    data = '%d번째 파일입니다.\n' % i
    fd.write(data)
    fd.close()
    
#파일 쓰기모드에서는 a는 추가 모드
fd = open('newFile.txt', 'a', encoding='utf-8')

for i in range(1, 21) :
    data = '%d번째 줄입니다.\n' % i
    fd.write(data)
fd.close()

with open('test.txt', 'a', encoding='utf-8') as test
    print('배고프다', file=fd)
    print('점심먹고싶다', file=fd)
    
with open('test.txt', encoding='utf=8') as file :
    ptest(file.read())

print('작업완료')
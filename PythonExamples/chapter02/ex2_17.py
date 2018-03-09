score=int(input('input your score:'))   #형변환 str->int

if 80 <= score <= 100:
    grade = 'A'
elif 60 <= score < 80:
    grade = 'B'
else:
    grade ='C'
    
print('Score %d is %s grade'%(score, grade))
print('삼항 연산')
num = int(input('Input number:'))
if num > 5:
    result = num*2
else:
    result = num+2  
print(result)

num = int(input('Input number again:'))
result = num*2 if num> 5 else num+2
print(result)

num = int(input('Input number one more time:'))
result = (num+2,num*2)[num>5]
print(result)

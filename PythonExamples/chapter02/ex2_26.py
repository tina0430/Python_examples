print('사전형 자료 처리')
price = {'사과':2000, '감':500, '바나나':1000} #판매 목록
shopping={'사과':2, '감':3}

#내가 산 과일의 가격과 내가 산 개수 출력
key = (i for i in shopping)
print(type(key)) #generator type
total = 0
for i in key : 
    count = int(shopping[i])
    
    print('내가 산 과일 %s %d개의 가격 : %d'%(i, count, int(price[i])*count))
    total += int(price[i])*count
#내가 산 과일 총액 출력
print('내가 구매한 과일의 값은 ', total)

print('리스트형 자료 처리')
import re
for testNum in ['111-1234-2342', '일이삼-사오육칠-팔구십', '123-456-7890'] :
    if re.match(r'^\d{3}-?\d{4}-?\d{4}', testNum):
        print(testNum, '는 전화번호가 맞을 수도!', sep='')
    else :
        print(testNum, '는 전화번호 아닌듯!', sep='')
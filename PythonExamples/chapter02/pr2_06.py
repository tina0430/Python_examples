#정수를 입력받아 홀짝 확인 하기. 0이 입력되면 반복문 종료

while True :
    number = int(input('확인할 숫자:'))
    if number == 0 :
        print('프로그램을 종료합니다.') 
        break
    elif number%2 == 0 : 
        print(number, '은(는) 짝수 입니다.', sep='')
    else : 
        print(number, '은(는) 홀수 입니다.', sep='')
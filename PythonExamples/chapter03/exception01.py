#try-except-finally 구문을 이용하여 에러(예외)처리

x = 4                               #1
y = 0                               #2 
list1 = [1,2,3]                     #3

try :                               #4
    z = x / y                       #5
    print(z)
    print('예외가 없을 경우 실행')
#err : 오류 정보를 담고있는 객체
except ZeroDivisionError as err :   #6
    pass                            #7
    print('error type :', err)      #8
    print('0으로 나누면 안돼요')          #9
finally :                           #10
    print('여기는 무조건 실행')           #11
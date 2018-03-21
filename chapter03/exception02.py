#try-except-finally 구문을 이용하여 에러(예외)처리

x = int(input('x값 입력 :'))
y = int(input('y값 입력 :'))
i = int(input('list index 입력 :'))
                               
list1 = [1,2,3]                     

try :                               
    print('list[', i, '] :', list1[i])
    z = x / y                       
    print('z :', z)
    print('예외가 없을 경우 실행')
    raise IndexError('에러메세지 조작')
#err : 오류 정보를 담고있는 객체
except ZeroDivisionError as err :   
    pass                            
    print('error type :', err)      
    print('0으로 나누면 안돼!')    
except IndexError as err : 
    print('error type :', err)      
    print('인덱스 초과 오류 발생')
except Exception as err :
    print('error type :', err)
else :
    print('예외상황 없이 정상 종료')      
finally :                           
    print('여기는 무조건 실행')
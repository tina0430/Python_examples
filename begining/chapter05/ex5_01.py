def devide(a, b):
    return a/b

print('이런 저런 작업을 하다가~')
c = devide(5, 2)
print(c)
print('계속 작업을 진행')

try :
    c = devide(5, 2)
    print(c)
    
    aa = [1, 2]
    print(aa[0])
except ZeroDivisionError:
    print('0으로 나누면 안 돼!')
except IndexError as err :
    print('참조 범위 오류 :', err)
except Exception as err :
    print('에러 발생 :', err)
finally :
    print('에러 유무에 상관 없이 반드시 수행')
        
print('다음 작업 계속')
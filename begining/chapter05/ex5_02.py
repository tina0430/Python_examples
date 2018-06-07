def positiveDevide(a, b) :
    if(b < 0) :
        raise NegativeDivisionError(b)  #강제 익셉션 발생
    return a/b

class NegativeDivisionError(Exception):
    def __init__(self, value) :
        self.value = value
        
print('프로그램 시작')
try :
    re = positiveDevide(10, 2)
    #re = positiveDevide(10, -2) #err1
    #re = positiveDevide(10, 0) #err2
    print('10/2 = {0}'.format(re))
except NegativeDivisionError as err1 :
    print('Error! Second argument is', err1.value)
except ZeroDivisionError as err2 :
    print('Error -', err2)
except Exception as err :
    print(err)
    
print('프로그램 끝!')
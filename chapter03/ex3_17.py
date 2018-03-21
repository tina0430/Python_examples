print('뭔가를 진행 하다가')
print('모듈 사용하기')

import sys
print('모듈 경로 :', sys.path)
#sys.exit() #프로그램 종료

print('\n수학 함수 읽기')
import math
print(math.pi)
print(math.sin(math.radians(30)))

print('\달력 출력하기')
import calendar
calendar.setfirstweekday(6) #일요일을 첫 요일로 설정
calendar.prmonth(2017, 1)   #출력 날자 설정
del calendar    #모듈 삭제
#calendar.prmonth(2015, 11) #에러 - 삭제된 모듈을 호출 할 수 없음

print('\n난수 출력하기')
import random
print(random.random())  #default : 0.0 <= v < 1.0
print(random.randrange(1, 10))
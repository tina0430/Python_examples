# 
# a = 14
# b = 5
# 
# sum = a+b 
# multiply = a*b 
# divide = a/b 
# remainder = a%b
# power = a-b
# 
# print('덧셈 :', sum)
# print('뺄셈 :', power)
# print('곱셈 :', multiply)
# print('나눗셈 : %7.6f'%(divide))
# print('나머지 :', remainder)
#
# jumin = '881120-1068234' 
# print('주민 번호 앞자리 :', jumin[:6])
# print('\n주민 번호 뒷자리 :', jumin[7:])
# 
# try :
#     myInput = int(input('정수 입력 : '))
#     if myInput%2 == 0 :
#         print('{}은(는) 짝수 이다'.format(myInput))
#     else :
#         print('{}은(는) 홀수 이다.'.format(myInput))
# except ValueError as err :
#     print('정수가 아닙니다.')
# 
# marks = [90, 25, 67, 45, 80]
# count = 1
# for i in marks :
#     if i >= 60 :
#         print('{}번째 응시자 {}점 합격'.format(count, i))
#     else :
#         print('{}번째 응시자 {}점 불합격'.format(count, i))
#     count += 1
# 
# source = open('sample.txt', 'r', encoding='utf-8')
# lines = source.readlines()
# total = 0
# count = 1
# 
# for i in lines :
#     total += int(i.replace('\n',''))
#     count += 1
# total /= count
# source.close()
# 
# result = open('result.txt', 'w', encoding='utf-8')
# result.write(str(total))
# result.close()
# import re
# 
# mylist = ['acccb', 'a....b', 'aaab', 'a.cccb']
# for i in mylist :
#     if re.match(r'a\.{3,}b', i):
#         print('패턴 %s : True'%i)
#     else :
#         print('패턴 %s : False'%i)

def isNum(num):
    try :
        float(num)
        return True
    except :
        return False
    
print(isNum(4))
print(isNum('4'))
print(isNum('s'))
print(isNum(''))
        

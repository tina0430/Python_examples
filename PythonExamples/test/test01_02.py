# 홍길동씨의 주민 등록 번호는 다음과 같다. 
# 슬라이싱(slicing)을 이용하여 다음 요구 사항을 풀어 보세요.

jumin = '871320-1068234'


print('홍길동씨가 태어난 년도는? : 19{}년'.format(jumin[:2]))
print('홍길동씨는 난자인가 여자인가? :', '남자' if jumin[7]=='1' else '여자')
print('홍길동씨의 생일은? : {}월 {}일'.format(jumin[2:4], jumin[4:6]))
print('홍길동씨의 주민번호 뒷자리 3개 :', jumin[-3:])
print('홍길동씨 주민번호 앞자리의 홀수번째 숫자들 :', jumin[:5:2])
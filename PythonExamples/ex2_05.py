s='sequence'    #s는 'sequence'란 str type객체를 참조한다
print()
print('길이(크기) :', len(s))
print('포함횟수 :', s.count('e'))
print('검색 위치1 :',s.find('e'), s.find('e', 3), s.rfind('e'))
# print('검색 위치2 :',s[2:].find('e'))
print('첫 글자 유무 :', s.startswith('s'), s.startswith('S'))

print()
ss='mbc'
print('mbc', id('mbc'), id(ss))
ss='abc'
print('abc', id('abc'), id(ss))

print()
print('슬라이싱---')
print(s[1:1], s[2:4])
print(s[1:], s[1:2])
print(s[:3], s[3:])
print(s[-1], s[-4:-1])
print(s[-4], s[::3])

print()
print('변경 전 :', id(s))
s='fre'+s[2:]
print(s)
print('변경 후:', id(s))
print(id('sequence'))

print()
s2='kbs mbc'
print(s2)
s2=' '+s2[:4]+'sbs '+s2[4:]
print(s2)

print()
print('문자열 공백 제거', s2.strip())
s3=s2.split(sep=' ', maxsplit=1)
print(s3)
s3=s2.split(sep=' ', maxsplit=2)
print(s3)

s3=s2.split(sep='b')
print(s3)
print('-'.join(s3))

s3=s2.split(sep=' ')
print(s3)
print('-'.join(s3))

print()
a='대한민국 만세'
b=a.replace('대한민국','파이썬')
print(b)
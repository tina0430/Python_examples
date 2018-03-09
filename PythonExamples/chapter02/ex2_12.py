import re

ss='1111234 abc가나다라ABC_555_6123 sdfg90 bc 1bc@bc%bc11'

print('01.', re.findall(r'123', ss))
print('02.', re.findall(r'가나다', ss))
print('03.', re.findall(r'[a-z]', ss))
print('04.', re.findall(r'[a-z]{2}', ss))
print('05.', re.findall(r'[0-9]', ss))
print('06.', re.findall(r'[0-9]{2}', ss))
print('07.', re.findall(r'[0-9]{2,3}', ss))
print('08.', re.findall(r'[abc]', ss))
print('09.', re.findall(r'.bc', ss))
print('10.', re.findall(r'[^1].+', ss))
print('11.', re.findall(r'[^1]+', ss))
print('12.', re.findall(r'^1+', ss))
print('13.', re.findall(r'1+', ss))
print('14.', re.findall(r'^1+', ss))
print('15.', re.findall(r'[0-9]*', ss))
print('16.', re.findall(r'[0-9]+', ss))
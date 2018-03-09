import os
from _dummy_thread import error

try:
    #f = OPEN(R'C:\경로명\ftest.txt')
    fdir = os.getcwd() #현재 모듈의 경로 얻기
    print(fdir)
    
    f=open(os.getcwd() + r'\ftest.txt')
    print(f)
    
    print(f.read())
    f.close()
    
    print('\파일의 일부분만 읽기')
    f = open(os.getcwd() + r'ftest.txt')
    for i in range(3) :
        line = f.readline()
        print(line, end =' ')
    f.close()
    
    print('\n부분행 읽기 - 슬라이싱')
    f = open(os.getcwd())
    lines = f.readlines()
    print(lines)
    f.close()
except Exception as err :
    print('파일 처리 오류 :', err) 
import os

print('환경 변수 출력 시작')
print(os.environ)
print('환경 변수 출력 끝\n')


os.chdir('c:\\work')
print('현재 위치 :', os.getcwd())

print('\n파일 읽기 시작')
print(os.system('pororo.txt'))
print('파일 읽기 끝\n')

fs = os.popen('dir')

print('fs.read() 시작')
print(fs.read())
print('fs.rea() 끝')
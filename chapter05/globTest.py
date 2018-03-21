import glob
import os

#디렉토리 이동
mydir = 'c:\\windows\\'
os.chdir(mydir)

#파일 이름 끝에 숫자가 있는 파일들 찾기
findfile = '*[0-9].*'
print(glob.glob(findfile))

#실행 가능한 exe 파일들만 조회
findfile = '*.exe'
print(glob.glob(findfile))
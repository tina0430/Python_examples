import os

def search (dirname) :
    try :
        #listdir함수는 지정된 디렉토리 내의 파일 목록을 리스트로 가져온다
        filelists = os.listdir(dirname)
        
        for onfile in filelists :
            #join함수는 디렉토리 이름과 파일 이름을 연결하여 전체 경로를 만들어 준다
            fullpathname = os.path.join(dirname, onfile)
            #
            if os.path.isdir(fullpathname) :
                search(fullpathname)
            else :
                ext = os.path.splitext(fullpathname)[-1]
                if ext == '.py' :
                    print(fullpathname)
    except PermissionError :
        pass #접근 권한이 없는 디렉토리에 대한 예외 처리
    
mydir = 'c:/'
#search(mydir)

for(path, dir, files) in os.walk('c:/') :
    for filename in files :
        ext = os.path.splitext(filename)[-1]
        if ext =='.py' :
            print('%s/%s' % (path, filename))

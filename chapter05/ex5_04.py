import os.path
try :
    letter = open(os.getcwd() + r'\ftest2.txt', mode='w')
    letter.write('Hi')
    letter.write('My friend')
    letter.close()
    
    letter = open(os.getcwd() + r'\ftest2.txt', mode='w')
    letter.write('hoho')
    letter.close()
    
    letter = open(os.getcwd() + r'\ftest2.txt', mode='a+')
    letter.write('\nHow have you been?')
    letter.write('I am good!')
    letter.close()
    
    letter = open(os.getcwd() + r'\ftest2.txt', mode='a+')
    letter.write('\nkeyboard')
    letter.write('\nmouse')
    letter.close()
    
    f2 = open(os.getcwd() + r'\ftest2.txt')
    print(f2.read())
    f2.close()
    
    print('\n----파일 목록 끊어 읽기----')
    from glob import glob
    #files = glob('*')           #현재 디렉토리에 있는 파일명 전부
    #files = glob('*.txt')       #확장자가 txt인 파일명
    files = glob('?????.txt')   #5자이고 txt인 파일명  
    for a in files :
        print(a)
        if os.path.isdir(a) : print('end')
except Exception as err :
    print(err)

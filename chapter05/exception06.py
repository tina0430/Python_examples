def sosiCheck(findData) :
    sosi = ['서현', '수영', '써니', '유리', '윤아', '태연', '티파니', '효연']
    ismember = False
    
    for member in sosi:
        if member ==findData :
            ismember = True
            break
    if ismember :
        print('소시가 맞네요')
    else :
        msg = '소시 맴버가 아니에요'
        raise Exception(msg)

name = input("이름을 입력하세요 :")
try :
    sosiCheck(name)
except Exception as err :
        print('예외 발생 :', name, err)
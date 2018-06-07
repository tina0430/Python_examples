try :
    source = open('a.txt', 'r',)
    target = open('b.txt', 'w', encoding='utf-8')
    mydata = source.readlines()
    
    for item in mydata :
        newdata = item.split(',')
        name = newdata[0]
        _gender = newdata[1]
        _score = newdata[2]
        if _gender == 'M':
            gender = '남자'
        else:
            gender = '여자'
    
        _score = float(_score)
        _score = int(_score)
        if _score % 2 == 0 :
            score = _score * 2
        else :
            score = _score * 3
            source.close()
        
        target.write(name+'/'+gender+'/'+str(score)+'\n')
        #print('{}/{}/{}'.format(name, gender, score), file=target)
    source.close()
    target.close()

except Exception as err :
    print(err)
print('작업 완료')

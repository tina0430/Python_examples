try :    
    source=open('jumsu.txt', 'r', encoding='utf-8')
    result=open('result.txt', 'w', encoding='utf-8')
    lists = source.readlines()
    for item in lists :
        temp = item.split(',')
        name = temp[0]
        korean = float(temp[1])
        english = float(temp[2])
        math = float(temp[3])
        total = korean+english+math
        average = total/3
        if temp[4] == 'F\n' : gender = '여자'
        else : gender = '남자'
        print(('%s/%s/%3.1f/%4.2f'%(name,gender,total,average)), file=result)
    source.close()
    result.close()
except Exception as err:
    print(err)
    
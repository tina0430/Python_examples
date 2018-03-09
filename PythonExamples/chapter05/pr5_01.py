import os

dong = input('동을 입력해주세요 :')
try :
    fdir=os.getcwd() 
    f = open(fdir+r'\zipcode.txt')
    datas = f.readlines()
    for i in datas :
        if (i.find(dong) != -1) :
            address = i.split('\t')
            print('[{}]{} {} {}'.format(address[0], address[1], \
                                        address[2], address[3].replace('\n', '')))
except Exception as err :
    print('에러 발생 :', err)
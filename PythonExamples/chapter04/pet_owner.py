from mypet import Pet

romeo = Pet('삽살이', 3, '사료')
juliet = Pet('야옹이', 4, '고등어')

try :
    f = open('삽살이와 야옹이', 'wt', encoding='utf-8')
    f.write(romeo.eat())
    f.write(romeo.sleep())
    f.write(juliet.eat())
    f.write(juliet.sleep())
    f.close
except Exception as err :
    print(err)

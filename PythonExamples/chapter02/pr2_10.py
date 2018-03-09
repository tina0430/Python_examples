#구구단 출력 2~9

for dan in range(2,10) :
    print('----%d단----'%dan)
    for i in range(1,10) :
        print('%d X %d = %2d'%(dan, i, i*dan))
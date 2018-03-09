print('여기는 커피 전문점입니다.')
print('커피는 아메리카노만 팔아요^^')
print('가격은 3000원입니다.')
print('오늘 은 커피가 3잔 남았습니다.')
print('=='*10)

coffee = 3
while True :
    money = int(input('지불할 금액 :'))
    if (money == 3000) :
        print('커피 맛있게 드세요')
        coffee-=1
    elif (money > 3000):
        print('거스름 돈은 %d원입니다.'%(money-3000))
        print('커피 맛있게 드세요')
        coffee-=1
    else:
        print('금액이 부족합니다.')
    
    print('남은 커피의 양은 %d잔 입니다.'%(coffee))
    if(not coffee) : 
            print('\n커피가 없어요~~. 장사 끝!!!')
            break
        
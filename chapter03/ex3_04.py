#전역, 지역 변수의 이해

player='전국대표'   #전역 변수

def funcSoccer(): 
    name='홍길동'
    player='지역대표'   
    print(name, player)
    #변수 우선순위에 의해 player는 지역대표 출력
    #지역변수 주석처리하면 전국대표 출력
    
print(funcSoccer)

funcSoccer()
    
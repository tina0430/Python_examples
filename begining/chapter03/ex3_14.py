#재귀함수 연습

def CountDown(n):
    if n == 0:
        print('완료')
        return 0
    else:
        print(n)
        return CountDown(n-1)
    
    
CountDown(5)
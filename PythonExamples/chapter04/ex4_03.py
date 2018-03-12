kor = 100   #전역변수

def abc() : #전역변수
    print('난 함수')
    
class My : 
    kor = 90
    
    def abc(self) :
        print('나는 My 클래스의 메소드 abc')
    
    def show(self) :
        #kor = 88
        print(self.kor)
        print(kor)  #13줄 주석을 풀면 지역변수 88 출력/주석처리하면 전역변수 100출력
        
        self.abc()
        abc()
        
m = My()
m.show()
from abc import ABCMeta, abstractmethod

#단계 1 : 추상 클래스 작성
#ABCMeta를 상속 받는다
class AbstractClass(metaclass=ABCMeta): #추상클래스
    
    #단계 2 : 데코레이터 @abstractmethod를 이용하여 장식해주어 추상함수로 만들어 준다.
    #추상 메소드
    @abstractmethod
    def abcMethod(self):
        pass
    
    #일반 메소드
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
#parent = AbsctClass()    #error
    
#단계 2 : 추상 메소드를 오버라이딩하지 않으면 오류 발생
class Child1(AbstractClass):
    name = '난 Child'
        
    def __init__(self):
        print('호호호')
    
    def abcMethod(self):
        pass
        
c1 = Child1()
class Pet :
    #생성자
    def __init__(self, name, sleeptime, feed) :
        self.name = name
        self.sleeptime = sleeptime
        self.feed = feed
        
    #기타 메서드
    def sleep(self) :
        return self.name + '가' + str(self.sleeptime) + '시간 동안 잠을 잡니다.\n'
        
    def eat(self) :
        return self.name + '가' + str(self.feed) + '를 먹습니다.\n'
class Fridge :
    isOpend = False
    foods=[]
    
    def open(self):
        self.isOpend = True
        print('냉장고 문 열기')
        
    def close(self):
        self.isOpend = False
        print('냉장고 문 닫기')
        
    def list(self):
        print('===냉장고 속 음식 리스트===')
        for i in self.foods :
            print('-', i.name, i.expiryDate)
        print()
        
    def put(self, thing):
        if self.isOpend :
            self.foods.append(thing)
            print('냉장고 속에 ',thing.name,'가(이) 들어감')
            self.list()
        else :
            print('냉장고 문이 닫혀있어서',thing.name,'가(이) 들어갈 수 없음!')

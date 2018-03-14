class Account:
    def __init__(self, name, balance, accountNo, bank):
        self.name = name
        self.balance = balance
        self.accountNo = accountNo
        self.bank = bank
        
    def Display(self):
        print('예금주 : ', self.name)
        print('예금주 : ', self.balance)
        print('계좌 번호 : ', self.accountNo)
        print('은행명 : ', self.bank)
        
soo = Account('김철수', 1000, '1234340', '국민은행')
hee = Account('박영희', 3000, '2342134', '우리은행')

soo.Display()
hee.Display()
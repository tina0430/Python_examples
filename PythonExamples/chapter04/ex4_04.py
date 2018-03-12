#class의 이해

class Singer:
    titleSong = '아리랑'   #맴버 변수
    def sing(self):
        msg = '노래는 '
        print(msg, self.titleSong, '랄랄라')
        
boys = Singer()
print('타이틀 송은 ', Singer.titleSong)
    
print('\nboys', end = ' ')
boys.sing()

print('girls', end = ' ')
girls = Singer()
girls.sing()
girls.titleSong = '댄싱퀸'
print('girls', end = ' ')
girls.sing()
print('girls', end = ' ')
girls.co = 'SM'
print('소속사 :', girls.co)

print('boys', end = ' ')
boys.sing()
#print('소속사 :', girls.co) #error

print()
print(boys, girls, Singer, sep = '\n')
print(id(boys), id(girls), id(Singer))
print(Singer.titleSong)
Singer.titleSong='아름다운 강산'
print('타이틀 송은 ', Singer.titleSong)
print('Singer Class song address :', id(Singer.titleSong))
print('boys', end = ' ')
boys.sing()
print('boys title song address :', id(boys.titleSong))
print('girls', end = ' ')
girls.sing()
print('girls title song address :', id(girls.titleSong))

print('Singer dict', end = ' ')
print(Singer.__dict__)
print('boys dict', end = ' ')
print(boys.__dict__)
print('girls dict', end = ' ')
print(girls.__dict__)
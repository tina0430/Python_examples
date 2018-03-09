a = 0
while a < 10:
    a+=1
    if a == 5: continue
    if a == 7: break
    print(a)
else:
    print('정상 종료하면 수행')

print('while 수행 후 a:', a)
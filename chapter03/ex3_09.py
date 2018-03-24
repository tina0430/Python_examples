#클로저(clouser) 연습

def outer(tax):
    def inner(count, price):
        amount = count*price*tax
        return amount
    return inner

tax_rate = outer(0.1)
mouse = tax_rate(5, 5000)
print('마우스 총액은', 5*5000)
print('세금은', mouse)

print()
usb = tax_rate(3, 1200)
print('usb 메모리 총액은', 3*1200)
print('세금은', usb)

print()
tax_rate2 = outer(0.05)
pencil = tax_rate2(2,1000)
print('연필 총액은', 2*1000)
print('세금은', pencil)
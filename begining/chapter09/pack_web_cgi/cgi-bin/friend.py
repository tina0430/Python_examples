import cgi

form = cgi.FieldStorage()

name = form["name"].value
phone= form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html\n')
print('''
<html>
    <head><meta charset="utf-8"></head>
    <body>
        <h2>이름은 {} 전화는 {} 성별은 {}</h2>
    </body>
</html>'''.format(name, phone, gen))
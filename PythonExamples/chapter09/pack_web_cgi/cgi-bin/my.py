import cgi

form = cgi.FieldStorage()
#FieldStorage는 사용자가 입력한 자료를 cgi에서 사용할 수 있도록 함.
name = form["name"].value
age= form["age"].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
    <body>
        이름은 {} 나이는 {}
    </body>
</html>'''.format(name, age))
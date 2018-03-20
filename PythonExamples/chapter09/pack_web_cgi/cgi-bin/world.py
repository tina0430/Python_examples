s1 = "자료1"
s2 = "자료2"

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
    <body>
        <h1>반가워요</h1>
            자료 출력 {0}, {1}
        <br/>
        <img src='../images/django.png' width='30%'/>
        <br/>
        <a href='../main.html'>메인으로</a>
    </body>
</html>'''.format(s1, s2))
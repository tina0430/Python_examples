import MySQLdb
from mariaDbConfig import config

print('Content-Type:html\n')
print('<html>')
print('<head><meta charset="utf-8"></head>')
print('<body>상품자료</p>')
print('<table border="1">')
print('<tr><td>코드</td><td>상품명</td><td>수량</td><td>단가</td></tr>')
try:
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    sql = "select * from sangdata"
    cur.execute(sql)
    datas = cur.fetchall()
    for item in datas:
        print('''
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(str(item[0]), str(item[1]), str(item[2]), str(item[3])))
    
except Exception as err:
    print('error :', err)

finally:
    cur.close()
    conn.close()

print('</table>')
print('</body>')
print('</html>')
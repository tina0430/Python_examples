import MySQLdb
from mariaDbConfig import config

print('Content-Type:html\n')
print('<html>')
print('<head><meta charset="utf-8"></head>')
print('<body>사원 정보</p>')
print('<table border="1">')
print('''
<tr>
    <td>번호</td>
    <td>이름</td>
    <td>부서</td>
    <td>직급</td>
    <td>성별</td>
</tr>''')
try:
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    sql = """
    select s.sawon_no, s.sawon_Name, b.buser_name, s.sawon_jik, s.sawon_gen 
    from sawon as s join buser as b
    where b.buser_no = s.buser_num"""
    cur.execute(sql)
    datas = cur.fetchall()
    for item in datas:
        print('''
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4])))
    
except Exception as err:
    print('error :', err)

finally:
    cur.close()
    conn.close()

print('</table>')
print('</body>')
print('</html>')
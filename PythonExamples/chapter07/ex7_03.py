import MySQLdb
from chapter07.mariaDbConfig import config  #자신에 맞게 수정할것

try :
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    
    sql = "select code, sang, su, dan from sangdata"
    cur.execute(sql)
    for data in cur.fetchall() :
        #print(data)
        print('%s %s %s %s'%data)
        
    print()
    cur.execute(sql)
    for r in cur:
        print(r[0], r[1], r[2], r[3])
        
    print()
    cur.execute(sql)
    for(code, sang, su, dan) in cur :
        print(code, sang, su, dan)
        
    sql = "insert into sangdata(code, sang,su,dan) values(%s, %s, %s, %s)"
    sql_data = (11, '상품', 5, 1000) 
    cur.execute(sql, sql_data)
    conn.commit()
    
    sql = "select * from sangdata"
    cur.execute(sql, sql_data)
    for r in cur:
        print(r[0], r[1], r[2], r[3])
        
except ZeroDivisionError as err:
    print('error : ', err)
    conn.rollback()
finally:
    conn.close()
    cur.close()



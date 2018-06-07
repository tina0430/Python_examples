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
        
    print('-'*30)
    cur.execute(sql)
    for r in cur:
        print(r[0], r[1], r[2], r[3])
        
    print('-'*30)
    cur.execute(sql)
    for(code, sang, su, dan) in cur :
        print(code, sang, su, dan)
        
    sql = "insert into sangdata(code, sang,su,dan) values(%s, %s, %s, %s)"
    sql_data = (11, '상품', 5, 1000) 
    cur.execute(sql, sql_data)
    conn.commit()
     
    print('-'*30)
    sql = "select * from sangdata"
    cur.execute(sql)
    for r in cur:
        print(r[0], r[1], r[2], r[3])
    
    print('-'*30)
    cur.execute(sql)
    for code, sang, su, dan in cur:
        print(code, sang, su, dan)
        
    sql = "update sangdata set sang=%s, su=%s, dan=%s where code = %s"
    sql_data=('파이썬', 7, 7000, 11)
    cur.execute(sql, sql_data)
    conn.commit()
    
    sql = "delete from sangdata where code = %s"
    cur.execute(sql, (11, ))
    conn.commit()    
    
except Exception as err:
    print('error : ', err)
    conn.rollback()
finally:
    conn.close()
    cur.close()



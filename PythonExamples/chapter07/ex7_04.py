import MySQLdb
import sys
from chapter07.mariaDbConfig import config

try :
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    
    buser = input('부서번호 입력')
    sql ="""
    select sawon_no, sawon_name, buser_num, sawon_jik
    from sawon 
    where buser_num={0}""".format(buser)
    
    cur.execute(sql)
    datas=cur.fetchall()
    
    if len(datas) == 0 :
        print(str(buser) + '번 부서는 없어용')
        sys.exit()  #프로그램 종료
        
    for sawon_no, sawon_name, buser_num, sawon_jik in datas :
        print(sawon_no, sawon_name, buser_num, sawon_jik)
        print('인원 수 : ', len(datas))
    conn.commit()    
except Exception as err:
    print('error : ', err)
    conn.rollback()
finally:
    conn.close()
    cur.close()

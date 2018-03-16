
import sqlite3

def process(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        
        sql = "create table sangpum(code integer primary key, sang txt, su text, dan text)"
        cur.execute(sql)
        
    except sqlite3.Error as err:
        print('error type : ', err)
        conn.rollback()
        
    finally:
        cur.close()
        conn.close()
    
if __name__ == '__main__' :
    process('nice.db')  #생성되는 DB 파일
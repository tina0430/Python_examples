import sqlite3

def process(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        
        #jikwon 테이블이 있으면 삭제
        sql = 'drop table if exists jikwon'
        cur.execute(sql)
        
        sql = "create table jikwon(id integer primary key, name text)"
        cur.execute(sql)
         
        sql = "insert into jikwon values(1, '한국인')"
        cur.execute(sql)
          
        sql = "insert into jikwon values(?,?)"
        cur.execute(sql, (2, '김칫국'))
         
        tdata = (3, '공깃밥')
        sql = "insert into jikwon values(?,?)"
        cur.execute(sql, tdata)
         
        tdatas = ((4, '공깃밥'),(5, '김밥'))
        cur.executemany(sql, tdatas)
 
        ldata = [6, '불고기 덮밥']
        cur.execute(sql, ldata)
         
        sql = 'insert into jikwon values(:sabun, :irum)'
        cur.execute(sql, {'sabun' :'7', 'irum':'이슬비'})
         
        ddata = {'irum':'소나기', 'sabun' :'8'}
        cur.execute(sql, ddata)
         
        ddata = {'irum':'장대비', 'sabun' :'9'}
        cur.execute(sql, ddata)
         
        sql = 'update jikwon set name = "홍길동" where id = 1'
        cur.execute(sql)
         
        sql = 'update jikwon set name = "고길동" where id = ?'
        cur.execute(sql, (2,))
         
        sql = 'update jikwon set name = "나길동" where id = ?'
        cur.execute(sql, [3])
        
         
        #수정 작업
        sql = "update jikwon set name='최길동' where id = 1"
        cur.execute(sql) 
        
        sql = "update jikwon set name='곽길동' where id = ?"
        cur.execute(sql, (2,))
        
        sql = "update jikwon set name='다길동' where id = ?"
        cur.execute(sql, [3])
        
        conn.commit()
        print('완료')
        
        sql = "select * from jikwon"
        cur.execute(sql)
        for row in cur :
            print(row)
            
        print()
        sql = "select * from jikwon where id <= 3"
        cur.execute(sql)
        datas = cur.fetchall()
        print(datas)
        
        sql = "select count(*) from jikwon"
        cur.execute(sql)
        print(cur.fetchone())
        
        
        sql = "SELECT name FROM jikwon WHERE id =20"
        cur.execute(sql)
        print(cur.fetchall())
        print(cur)
        
    except sqlite3.Error as err:
        print('error type : ', err)
        conn.rollback()
        
    finally:
        cur.close()
        conn.close()
    
if __name__ == '__main__' :
    process('nice.db')  #생성되는 DB 파일
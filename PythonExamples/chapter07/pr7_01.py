# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sqlite3

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
    dbName = 'sangpum.db'
    def __init__( self, parent ):
        self.initUI(parent)
        self.Center()
        self.dbLoad()

    def initUI(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        #panel1 & bsizer1
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblSang = wx.StaticText( self.panel1, wx.ID_ANY, u"상품명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblSang.Wrap( -1 )
        bSizer1.Add( self.lblSang, 0, wx.ALL, 5 )
        
        self.txtSang = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txtSang, 1, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.panel1, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtSu = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        bSizer1.Add( self.txtSu, 1, wx.ALL, 5 )
        
        self.lblDan = wx.StaticText( self.panel1, wx.ID_ANY, u"단가 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblDan.Wrap( -1 )
        bSizer1.Add( self.lblDan, 0, wx.ALL, 5 )
        
        self.txtDan = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        bSizer1.Add( self.txtDan, 1, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.btnInsert, 1, wx.ALL, 5 )
        
        
        self.panel1.SetSizer( bSizer1 )
        self.panel1.Layout()
        bSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        #panel2 & bsizer2
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstView = wx.ListCtrl( self.panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        
        bSizer2.Add( self.lstView, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        #panel3 & bsizer3
        self.panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staCount = wx.StaticText( self.panel3, wx.ID_ANY, u"건수 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer3.Add( self.staCount, 0, wx.ALL, 5 )
        
        self.lblCount = wx.StaticText( self.panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblCount.Wrap( -1 )
        bSizer3.Add( self.lblCount, 0, wx.ALL, 5 )
        
        
        self.panel3.SetSizer( bSizer3 )
        self.panel3.Layout()
        bSizer3.Fit( self.panel3 )
        bSizer.Add( self.panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnInsert.Bind( wx.EVT_BUTTON, self.onInsert )
                
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def onInsert( self, event ):
        try :
            conn = sqlite3.connect(self.dbName)
            cur = conn.cursor()
            
            name = self.txtSang.GetValue()
            count = self.txtSu.GetValue()
            price = self.txtDan.GetValue()
            
            #입력 오류
            if name == '' :
                wx.MessageBox('상품명을 입력해주세요', '상품명 입력 오류', wx.OK)
                self.txtSang.SetFocus()
            elif count == '' :     
                wx.MessageBox('상품 수량을 입력해주세요', '상품 수량 입력 오류', wx.OK)
                self.txtSu.SetFocus()
            elif price == '' :   
                wx.MessageBox('상품 단가를 입력해주세요', '상품 단가 입력 오류', wx.OK)
                self.txtDan.SetFocus()
                
            #상품명과 단가로 코드 select
            sql = "select exists(select * from sangpum where Sang = ? and Dan = ?)"
            cur.execute(sql, (name, price))
            temp = cur.fetchone()
            
            #상품 있으면 수량만 올리고
            if temp[0] == 1 :
                sql = "update sangpum set su=(su+?) where Sang = ? and Dan = ?"
                cur.execute(sql, (count, name, price))
                
            #코드 없으면 max 써서 코드 생성하고 insert 
            else :
                sql = "select max(code) from sangpum"
                cur.execute(sql)
                code = cur.fetchone()[0]+1
                newDatas = (code, name, count, price)
                sql = "insert into sangpum values(?, ?, ?, ?)"
                cur.execute(sql, newDatas)
                #self.lstView.RefreshItem()
                
            conn.commit()
            wx.MessageBox('상품이 정상적으로 추가되었습니다.', '추가 성공', wx.OK)
            
            #전체 코드 몇개인지 count
            sql = "select count(*) from sangpum"
            cur.execute(sql)
            count = cur.fetchone()[0]+1
            self.lblCount.SetLabel(str(count))
            
        except sqlite3.Error as err:
            print('error type : ', err)
            conn.rollback()
        
        finally:
            cur.close()
            conn.close()
            self.dbLoad()
            self.txtSang.SetValue('')
            self.txtSu.SetValue('')
            self.txtDan.SetValue('')
            self.txtSang.SetFocus() 
            
    def dbLoad(self):
        
        self.lstView.ClearAll()
        self.lstView.InsertColumn(0, '코드', width = 50)
        self.lstView.InsertColumn(1, '상품명', width = 100)
        self.lstView.InsertColumn(2, '수량', width = 50)
        self.lstView.InsertColumn(3, '단가', width = 100)
        self.lstView.InsertColumn(4, '금액', width = 100)
        
        try :
            conn = sqlite3.connect(self.dbName)
            cur = conn.cursor()
        
            #db에 있는 열 리스트에 추가
            sql = "select * from sangpum"
            cur.execute(sql)
            for row in cur :
                i = self.lstView.InsertItem(1000, 0)
                self.lstView.SetItem(i, 0, str(row[0]))
                self.lstView.SetItem(i, 1, str(row[1]))
                self.lstView.SetItem(i, 2, str(row[2]))
                self.lstView.SetItem(i, 3, str(row[3]))
                temp = int(row[3])*int(row[2])
                self.lstView.SetItem(i, 4, str(temp))
                
            sql = "select count(*) from sangpum"
            cur.execute(sql)
            count = cur.fetchone()[0]
            self.lblCount.SetLabel(str(count))
                
        except sqlite3.Error as err:
            print('error type : ', err)
            conn.rollback()
        
        finally:
            cur.close()
            conn.close()
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None).Show()
    app.MainLoop()



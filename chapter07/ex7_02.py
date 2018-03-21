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
    dbName = 'nice.db'
    
    def __init__( self, parent ):
        self.initUI(parent)
        self.Center()
        self.dbLoad()
    
    def __del__( self ):
        pass
    
    def initUI(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'Sqlite 사용', pos = wx.DefaultPosition, size = wx.Size( 380,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblId = wx.StaticText( self.panel1, wx.ID_ANY, u"id :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblId.Wrap( -1 )
        bSizer1.Add( self.lblId, 0, wx.ALL, 5 )
        
        self.txtId = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer1.Add( self.txtId, 0, wx.ALL, 5 )
        
        self.lblName = wx.StaticText( self.panel1, wx.ID_ANY, u"Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblName.Wrap( -1 )
        bSizer1.Add( self.lblName, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer1.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.panel1, wx.ID_ANY, u"추가", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer1.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        
        self.panel1.SetSizer( bSizer1 )
        self.panel1.Layout()
        bSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstData = wx.ListCtrl( self.panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT )
        bSizer2.Add( self.lstData, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        #lstData의 표제 설정
        self.lstData.ClearAll()
        self.lstData.InsertColumn(0, 'id', width = 100)
        self.lstData.InsertColumn(1, 'Name', width = 225)
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnInsert.Bind( wx.EVT_BUTTON, self.OnBtnInsert )
    
    def dbLoad(self):
        try :
            conn = sqlite3.connect(self.dbName)
            cur = conn.cursor()
        
            sql = "select * from jikwon"
            cur.execute(sql)
            for row in cur :
                i = self.lstData.InsertItem(1000, 0)
                self.lstData.SetItem(i, 0, str(row[0]))
                self.lstData.SetItem(i, 1, str(row[1]))
                
        except sqlite3.Error as err:
            print('error type : ', err)
            conn.rollback()
        
        finally:
            cur.close()
            conn.close()

    # Virtual event handlers, overide them in your derived class
    def OnBtnInsert( self, event ):
        newId = self.txtId.GetValue()
        newName = self.txtName.GetValue()
        
        try:
            conn = sqlite3.connect(self.dbName)
            cur = conn.cursor()
            print(int(newId))
            sql = "select exists(select * from jikwon where id = ?)"
            
            cur.execute(sql, (newId,))
            i = cur.fetchone()
            if i[0] == 0:
                newDatas = (newId, newName)
                sql = "insert into jikwon values(?, ?)"
                cur.execute(sql, newDatas)
                conn.commit()
                wx.MessageBox('성공적으로 추가되었습니다.', '입력 오류', wx.OK)
            else :
                wx.MessageBox('이미 존재하는 아이디 입니다.', '입력 오류', wx.OK)
            
        except ZeroDivisionError as err:
            print('error type : ', err)
            conn.rollback()
        
        finally:
            cur.close()
            conn.close()
            self.dbLoad()
            self.txtId.SetValue('')
            self.txtName.SetValue('')
            self.txtId.SetFocus()        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None).Show()
    app.MainLoop()

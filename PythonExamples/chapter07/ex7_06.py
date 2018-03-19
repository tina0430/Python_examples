import wx
import wx.xrc
import MySQLdb
import sys
from chapter07.mariaDbConfig import config

class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        self.initUI(parent)
        self.viewListData()
        self.Center(wx.BOTH)
        
    def initUI(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblNo = wx.StaticText( self.panel1, wx.ID_ANY, u"번호 :", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.lblNo.Wrap( -1 )
        bSizer1_1.Add( self.lblNo, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer1_1.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer1_1.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer1_1, 1, wx.EXPAND, 5 )
        
        bSizer1_2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblName = wx.StaticText( self.panel1, wx.ID_ANY, u"이름 :", wx.Point( 1,0 ), wx.DefaultSize, 0 )
        self.lblName.Wrap( -1 )
        bSizer1_2.Add( self.lblName, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.Point( 1,1 ), wx.DefaultSize, 0 )
        bSizer1_2.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnUpdate = wx.Button( self.panel1, wx.ID_ANY, u"수정", wx.Point( 1,2 ), wx.Size( 45,-1 ), 0 )
        bSizer1_2.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnConfirm = wx.Button( self.panel1, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
        self.btnConfirm.Enable(enable=False)
        bSizer1_2.Add( self.btnConfirm, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer1_2, 1, wx.EXPAND, 5 )
        
        bSizer1_3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblTel = wx.StaticText( self.panel1, wx.ID_ANY, u"전화 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblTel.Wrap( -1 )
        bSizer1_3.Add( self.lblTel, 0, wx.ALL, 5 )
        
        self.txtTel = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1_3.Add( self.txtTel, 0, wx.ALL, 5 )
        
        self.btnDel = wx.Button( self.panel1, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer1_3.Add( self.btnDel, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer1_3, 1, wx.EXPAND, 5 )
        
        
        self.panel1.SetSizer( bSizer1 )
        self.panel1.Layout()
        bSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstMem = wx.ListCtrl( self.panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer2.Add( self.lstMem, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staCnt = wx.StaticText( self.panel3, wx.ID_ANY, u"인원수 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCnt.Wrap( -1 )
        bSizer3.Add( self.staCnt, 0, wx.ALL, 5 )
        
        self.lblCnt = wx.StaticText( self.panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblCnt.Wrap( -1 )
        bSizer3.Add( self.lblCnt, 0, wx.ALL, 5 )
        
        
        self.panel3.SetSizer( bSizer3 )
        self.panel3.Layout()
        bSizer3.Fit( self.panel3 )
        bSizer.Add( self.panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.lstMem.InsertColumn(0, '번호', width = 50)
        self.lstMem.InsertColumn(1, '이름', width = 100)
        self.lstMem.InsertColumn(2, '전화', width = 100)
        
        self.btnInsert.id = 1; self.btnUpdate.id = 2
        self.btnConfirm.id = 3; self.btnDel.id = 4
        
        self.btnInsert.Bind( wx.EVT_BUTTON, self.onClick )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.onClick )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.onClick )
        self.btnDel.Bind( wx.EVT_BUTTON, self.onClick )
        self.viewListData()
    
    def viewListData(self):
        try :
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            sql = "select * from pymem"
            cur.execute(sql)
            self.lstMem.DeleteAllItems()
            datas = cur.fetchall()
            
            for no, name, tel in datas:
                i = self.lstMem.InsertItem(sys.maxsize, 0)
                self.lstMem.SetItem(i, 0, str(no))
                self.lstMem.SetItem(i, 1, str(name))
                self.lstMem.SetItem(i, 2, str(tel))
            
            self.lblCnt.SetLabel(str(len(datas)))

        except ZeroDivisionError as err :
            print("error type : ", err)
        finally:
            cur.close()
            conn.close()
            
    def onClick(self, event):
            btnID = event.GetEventObject().id
            if btnID == 1 :
                self.memInsert()
            elif btnID == 2 :
                self.memUpdate()
            elif btnID == 3 :
                self.memUpdateConfirm()
            elif btnID == 4 :
                self.memDel()
            elif btnID == 5 :
                self.memUpdateCancel()
            
    def memInsert(self):
        try :
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            no = self.txtNo.GetValue()
            name = self.txtName.GetValue()
            tel = self.txtTel.GetValue() 
            
            if no == '' :
                wx.MessageBox("번호를 입력하세요", "번호 입력 오류", wx.OK)
                self.txtNo.SetFocus()
                return 0
                
            elif name == '' :
                wx.MessageBox("이름을 입력하세요", " 이름 입력 오류", wx.OK)
                self.txtName.SetFocus()
                return 0
                
            elif tel == '':
                wx.MessageBox("전화번호를 입력하세요", "전화번호 입력 오류", wx.OK)
                self.txtTel.SetFocus()
                return 0
                
            else :
                if self.selectNo(no):
                    wx.MessageBox("중복된 번호를 입력하였습니다.", "번호 입력 오류", wx.OK)
                    self.txtNo.SetFocus()
                    return 0
                    
                elif self.selectTel(tel):
                    wx.MessageBox("중복된 전화번호를 입력하였습니다.", "전화번호 입력 오류", wx.OK)
                    self.txtTel.SetFocus()
                    return 0
                 
                else:
                    sql = "insert into pymem(id, name,tel) values(%s, %s, %s)"
                    cur.execute(sql, (no, name, tel))
                    conn.commit()
                    wx.MessageBox("자료가  등록되었습니다.", "정보 등록 완료", wx.OK)
                
                    self.viewListData()
                    self.txtNo.SetValue('')
                    self.txtName.SetValue('')
                    self.txtTel.SetValue('')
                    self.txtNo.SetFocus()
                                          
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            
        except Exception as err:
            print('error type :', err)
            conn.rollback()
            
        finally:
            cur.close()
            conn.close()
            
    def selectNo(self, no):
        try :
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            sql = "select * from pymem where id = %s"
            cur.execute(sql, (no,))
            temp = cur.fetchone()
            
            return temp
            
        except ZeroDivisionError as err:
            print('error type : ', err)
            
        finally:
            cur.close()
            conn.close()
            
    def selectTel(self, tel):
        try :
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            sql = "select exists(select tel from pymem where tel =%s)"
            cur.execute(sql, (tel,))
            temp = cur.fetchone()
            
            if temp[0] == 1 : 
                return True 
            else : 
                return False 
            
        except ZeroDivisionError as err:
            print('error type :', err)
        finally:
            cur.close()
            conn.close()
        
    def memUpdate(self):
        dlg = wx.TextEntryDialog(None, '수정할 번호를 입력하세요', '수정')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == "":
                return 0
            upID = dlg.GetValue()
            data = self.selectNo(upID)
            if not data:
                wx.MessageBox(upID+'번은 등록된 자료가 아닙니다.', '수정 오류')
                return 0
            
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(str(data[1]))
            self.txtTel.SetValue(str(data[2]))
            self.txtNo.SetEditable(False)
            self.btnConfirm.Enable(True)
            self.btnUpdate.SetLabel('취소')
            self.btnUpdate.id = 5
        
        else: 
            return 0
        
        dlg.Destroy()
    
    def memUpdateConfirm(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        try :
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            if self.selectTel(tel):
                wx.MessageBox("중복된 전화번호를 입력하였습니다.", "전화번호 입력 오류", wx.OK)
                self.txtTel.SetFocus()
                return 0
                
            sql = "update pymem set name = %s, tel = %s where id = %s"
            cur.execute(sql, (name, tel, no))
            conn.commit()
            
            self.viewListData()
            self.memUpdateCancel()
            
        except Exception as err:
            print('error', err)
            conn.rollback
        finally:
            cur.close()
            conn.close()
    
    def memUpdateCancel(self):
            self.txtNo.SetValue("")
            self.txtName.SetValue("")
            self.txtTel.SetValue("")
            self.txtNo.SetEditable(True)
            self.btnUpdate.SetLabel('수정')
            self.btnUpdate.id = 2
            self.btnConfirm.Enable(False)
    
    def memDel(self):
        dlg = wx.TextEntryDialog(None, '삭제할 번호를 입력하세요', '삭제')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == "":
                wx.MessageBox('삭제할 자료의 번호를 입력해주세요', '삭제 오류', wx.OK) 
                return 0
            
            delID = dlg.GetValue()
            
            if not self.selectNo(delID):
                wx.MessageBox(delID +'번은 등록된 자료가 아닙니다.', '삭제 오류', wx.OK)
                return 0
        
            try :
                conn = MySQLdb.connect(**config)
                cur = conn.cursor()
            
                sql = "delete from pymem where id = %s"
                cur.execute(sql, (delID,))
                conn.commit()
                wx.MessageBox('자료가 삭제되었습니다.', '삭제 완료', wx.OK)
                self.viewListData()
            
            except Exception as err:
                print('error', err)
                conn.rollback()
            finally:
                cur.close()
                conn.close()
        else : return
    
        dlg.Destroy()

if __name__ == "__main__" :
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()
    
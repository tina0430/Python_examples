import MySQLdb
import sys
import re
import wx
import wx.xrc
from chapter07.mariaDbConfig import config

class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        self.initUI(parent)
    
    def __del__( self ):
        pass
    
    def initUI(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblInsert = wx.StaticText( self.panel1, wx.ID_ANY, u"직급 입력 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblInsert.Wrap( -1 )
        bSizer1.Add( self.lblInsert, 0, wx.ALL, 5 )
        
        self.txtJik = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txtJik, 0, wx.ALL, 5 )
        
        self.btnSearch = wx.Button( self.panel1, wx.ID_ANY, u"검색", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.btnSearch, 0, wx.ALL, 5 )
        
        
        self.panel1.SetSizer( bSizer1 )
        self.panel1.Layout()
        bSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 0, wx.ALL|wx.EXPAND, 5 )
        
        ###############
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.txtList = wx.TextCtrl( self.panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer2.Add( self.txtList, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnSearch.Bind( wx.EVT_BUTTON, self.onInsearch )
    
    # Virtual event handlers, overide them in your derived class
    
    def onInsearch( self, event ):
        try : 
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
        
            jik = self.txtJik.GetValue()
            if not re.match('[가-힣]{2,}', jik) :
                wx.MessageBox('직급은 두 글자 이상, 한글로 입력해주세요', '직급 입력 오류', wx.OK)
                self.txtJik.SetFocus()
            else :
                sql = """
                select sawon_no, sawon_name, sawon_jik, sawon_pay from sawon where sawon_jik like '{}%';
                """.format(jik)
                cur.execute(sql)                
                for sawon_no, sawon_name, sawon_jik, sawon_pay in cur:
                    self.txtList.AppendText("[{}] {} {} {}\n".format(sawon_no, sawon_name, sawon_jik, sawon_pay))
        except Exception as err :
            pass
        finally : 
            cur.close()
            conn.close()
            
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None).Show()
    app.MainLoop()
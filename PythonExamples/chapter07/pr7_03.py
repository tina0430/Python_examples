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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = '사원 조회', pos = wx.DefaultPosition, size = wx.Size( 300,280 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.rbAll = wx.RadioButton( self.panel1, wx.ID_ANY, u"전체", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.rbAll, 0, wx.ALL, 5 )
        
        self.rbM = wx.RadioButton( self.panel1, wx.ID_ANY, u"남", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.rbM, 0, wx.ALL, 5 )
        
        self.rbF = wx.RadioButton( self.panel1, wx.ID_ANY, u"여", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.rbF, 0, wx.ALL, 5 )
        
        
        self.panel1.SetSizer( bSizer1 )
        self.panel1.Layout()
        bSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.txtSawon = wx.TextCtrl( self.panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer2.Add( self.txtSawon, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.rbAll.Id=1; self.rbM.Id=2; self.rbF.Id=3;  
        self.rbAll.Bind( wx.EVT_RADIOBUTTON, self.onClick )
        self.rbM.Bind( wx.EVT_RADIOBUTTON, self.onClick )
        self.rbF.Bind( wx.EVT_RADIOBUTTON, self.onClick )
    
    def onClick( self, event ):
        try : 
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            rbIds = event.GetEventObject().Id
            sql = """
                select s.sawon_no, s.sawon_name, b.buser_name, s.sawon_jik
                from sawon as s join buser as b
                on s.buser_num = b.buser_no"""
            if rbIds == 2:
                sql += " and s.sawon_gen = '남'"
            elif rbIds == 3:
                sql += " and s.sawon_gen = '여'"
                
            cur.execute(sql)
            data = cur.fetchall()
            line = "사번\t이름\t부서명\t직급\n"+("-"*40)+'\n'
            self.txtSawon.SetValue(line)
            for item in data:
                line = "{}\t{}\t{}\t{}\n".format(item[0], item[1], item[2], item[3])
                self.txtSawon.AppendText(line)
        except Exception as err :
            pass
        finally : 
            cur.close()
            conn.close()
            
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
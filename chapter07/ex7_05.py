import wx
import wx.xrc
import MySQLdb
from chapter07.mariaDbConfig import config

class MyFrame(wx.Frame):
    def __init__(self, parent):
        self.initUI(parent)
        self.Center(wx.BOTH)
    
    def initUI(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 358,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 3, 4, 5, 5 )
        
        self.lblCode = wx.StaticText( self.panel1, wx.ID_ANY, u"코드 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblCode.Wrap( -1 )
        gSizer1.Add( self.lblCode, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.txtCode = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        gSizer1.Add( self.txtCode, 0, wx.ALL, 5 )
        
        self.lblName = wx.StaticText( self.panel1, wx.ID_ANY, u"   품명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblName.Wrap( -1 )
        gSizer1.Add( self.lblName, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        gSizer1.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.lblQuantity = wx.StaticText( self.panel1, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblQuantity.Wrap( -1 )
        gSizer1.Add( self.lblQuantity, 0, wx.ALL, 5 )
        
        self.txtQuantity = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        gSizer1.Add( self.txtQuantity, 0, wx.ALL, 5 )
        
        self.lblUnitPrice = wx.StaticText( self.panel1, wx.ID_ANY, u"   단가 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblUnitPrice.Wrap( -1 )
        gSizer1.Add( self.lblUnitPrice, 0, wx.ALL, 5 )
        
        self.txtUnitPrice = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        gSizer1.Add( self.txtUnitPrice, 0, wx.ALL, 5 )
        
        self.staPrice = wx.StaticText( self.panel1, wx.ID_ANY, u"금액 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staPrice.Wrap( -1 )
        gSizer1.Add( self.staPrice, 0, wx.ALL, 5 )
        
        self.lblPrice = wx.StaticText( self.panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblPrice.Wrap( -1 )
        gSizer1.Add( self.lblPrice, 0, wx.ALL, 5 )
        
        
        self.panel1.SetSizer( gSizer1 )
        self.panel1.Layout()
        gSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 0, wx.ALL, 5 )
        
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.panel2, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.Size( 75,25 ), 0 )
        bSizer2.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( 75,25 ), 0 )
        bSizer2.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.Size( 75,25 ), 0 )
        bSizer2.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.panel2, wx.ID_ANY, u">||", wx.DefaultPosition, wx.Size( 75,25 ), 0 )
        bSizer2.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Id = 1; self.btn2.Id = 2 
        self.btn3.Id = 3; self.btn4.Id = 4 
        self.btn1.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn2.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn3.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn4.Bind( wx.EVT_BUTTON, self.onClick )
    def dbLoad(self):
        try :
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            sql = "select * from sangdata"
            cur.execute(sql)
            global datas
            datas = cur.fetchall()
            self.SetDatas()
            
        except ZeroDivisionError as err:
            print('error', err)
        finally:
            cur.close()
            conn.close()
        
    def onClick(self, event):
        try :
            btnID = event.GetEventObject().id
            conn = MySQLdb.connect(**config)
            cur = conn.cursor()
            
            sql = ""
            cur.execute(sql)
            
        except ZeroDivisionError as err:
            print('error', err)
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__" :
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()
    
 


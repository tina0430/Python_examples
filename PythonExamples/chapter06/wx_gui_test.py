# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame ( wx.Frame ):
    
    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
#         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblName = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblName.Wrap( -1 )
        bSizer2.Add( self.lblName, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtName, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lblAge = wx.StaticText( self.m_panel2, wx.ID_ANY, u"나이 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblAge.Wrap( -1 )
        bSizer5.Add( self.lblAge, 0, wx.ALL, 5 )
        
        self.txtAge = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.txtAge, 0, wx.ALL, 5 )
        
        self.btnOk = wx.Button( self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btnOk, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer5 )
        self.m_panel2.Layout()
        bSizer5.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.staShow = wx.StaticText( self.m_panel3, wx.ID_ANY, u"결과보기", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staShow.Wrap( -1 )
        bSizer6.Add( self.staShow, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer6 )
        self.m_panel3.Layout()
        bSizer6.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.showData )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def showData( self, event ):
        name = self.txtName.GetValue()
        age = self.txtAge.GetValue()
        self.staShow.SetLabel(name + age)
        wx.MessageBox('%s씨의 나이는 %s세'%(name, age), '결과', wx.OK)
        event.Skip()
    
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title = '이름과 나이 입력').Show()
    app.MainLoop()


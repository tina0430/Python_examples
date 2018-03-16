# # -*- coding: utf-8 -*- 
# 
# ###########################################################################
# ## Python code generated with wxFormBuilder (version Jun 17 2015)
# ## http://www.wxformbuilder.org/
# ##
# ## PLEASE DO "NOT" EDIT THIS FILE!
# ###########################################################################
# 
# import wx
# import wx.xrc
# 
# ###########################################################################
# ## Class ex6_05Frame
# ###########################################################################
# 
# class MyFrame (wx.Frame):
#     
#     def __init__( self, parent ):
#         wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"거래처 관리", pos = wx.DefaultPosition, size = wx.Size( 490,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
#         
#         bSizer = wx.BoxSizer( wx.VERTICAL )
#         bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
#         bSizer2 = wx.BoxSizer( wx.VERTICAL )
#         bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
#         
#         self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#         self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#         self.panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#         
#         self.lblName = wx.StaticText( self.panel1, wx.ID_ANY, u"거래처 명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.lblName.Wrap( -1 )
#         bSizer1.Add( self.lblName, 0, wx.ALL, 5 )
#         
#         self.txtName = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer1.Add( self.txtName, 0, wx.ALL, 5 )
#         
#         self.lblTel = wx.StaticText( self.panel1, wx.ID_ANY, u"전화 :", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.lblTel.Wrap( -1 )
#         bSizer1.Add( self.lblTel, 0, wx.ALL, 5 )
#         
#         self.txtTel = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer1.Add( self.txtTel, 0, wx.ALL, 5 )
#         
#         self.btnRegist = wx.Button( self.panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer1.Add( self.btnRegist, 0, wx.ALL, 5 )
#         
#         self.panel1.SetSizer( bSizer1 )
#         self.panel1.Layout()
#         bSizer1.Fit( self.panel1 )
#         bSizer.Add( self.panel1, 1, wx.EXPAND |wx.ALL, 5 )
#         
#         self.lstPartner = wx.ListCtrl( self.panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
#         bSizer2.Add( self.lstPartner, 1, wx.ALL|wx.EXPAND, 5 )
# 
#         self.panel2.SetSizer( bSizer2 )
#         self.panel2.Layout()
#         bSizer2.Fit( self.panel2 )
#         bSizer.Add( self.panel2, 1, wx.EXPAND |wx.ALL, 5 )
#         
#         self.lstPartner = wx.ListCtrl( self.panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
#         bSizer3.Add( self.lstPartner, 0, wx.ALL, 5 )
#         
#         self.lblCount = wx.StaticText( self.panel3, wx.ID_ANY, u" 0", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.lblCount.Wrap( -1 )
#         bSizer3.Add( self.lblCount, 0, wx.ALL, 5 )
#         
#         self.panel3.SetSizer( bSizer3 )
#         self.panel3.Layout()
#         bSizer3.Fit( self.panel3 )
#         bSizer.Add( self.panel3, 1, wx.EXPAND |wx.ALL, 5 )
#         
#         self.SetSizer( bSizer )
#         self.Layout()
#     
#         self.lstPartner.InsertColumn(0, '거래처 이름', width=200)
#         self.lstPartner.InsertColumn(1, '전화번호', width=200)
#         
#         self.lblPartner = wx.StaticText( self.panel3, wx.ID_ANY, u" 거래처 수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.lblPartner.Wrap( -1 )
#         bSizer4.Add( self.lblPartner, 0, wx.ALL, 5 )
#         
#         self.lblCount = wx.StaticText( self.panel3, wx.ID_ANY, u" 0", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.lblCount.Wrap( -1 )
#         bSizer4.Add( self.lblCount, 0, wx.ALL, 5 )
#         
#         self.panel3.SetSizer( bSizer4 )
#         self.panel3.Layout()
#         bSizer4.Fit( self.panel3 )
#         bSizer1.Add( self.panel3, 1, wx.EXPAND |wx.ALL, 5 )
#         
#         
#         self.SetSizer( bSizer1 )
#         self.Layout()
#         
#         self.Centre( wx.BOTH )
#     
#         # Connect Events
#         self.btnRegist.Bind( wx.EVT_BUTTON, self.onClick )
#         
#     def __del__( self ):
#         pass
#     
#     def onClick( self, event ) :
#         name = self.txtName.GetValue()
#         tel = self.txtTel.GetValue()
#         
#         i = self.lstPartner.InsertItem(1000, 0)
#         self.lstPartner.SetItem(i, 0, name)
#         self.lstPartner.SetItem(i, 1, tel)
#         
#         #전체 건수 표시
#         self.lblCount = str(self.lstPartner.GetItemCount())
#         
#         self.txtName.SetValue('')
#         self.txtTel.SetValue('')
#         self.txtName.SetFocus()
#         
# if __name__ == '__main__':
#     app = wx.App()
#     MyFrame(None).Show()
#     app.MainLoop()

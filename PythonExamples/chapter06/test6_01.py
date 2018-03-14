import wx

app = wx.App()

frame = wx.Frame(None, title='윈도우 창')
frame.Center(True)
frame.Show(True)

app.MainLoop()
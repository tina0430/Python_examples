#프레임에 메뉴 추가

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        #윈도우 제목, 너비와 높이를 설정
        super(Example, self).__init__(parent, title=title, size=(300,250))
        
        #프레임 컨트롤 추가 -----
        #self.txtA = wx.TextCtrl(self)
        self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
        #상태 표시줄 생성
        self.CreateStatusBar()
        
        #프레임에 메뉴 추가하여 작업 -----
        menuBar = wx.MenuBar()
        menuFile = wx.Menu()
        
        #메뉴 아이템 설정1
        menuNew = wx.MenuItem(menuFile, wx.ID_NEW, 'New', 'New document')
        menuFile.Append(menuNew)
        
        #메뉴 아이템 설정2
        menuOpen = menuFile.Append(wx.ID_OPEN, 'Open', 'Document open')
        
        #구분선 추가
        menuFile.AppendSeparator()
        
        #메뉴 아이템 설정3
        menuExit = menuFile.Append(wx.ID_EXIT, 'Exit', 'Exit program')
        
        #메뉴 그룹을 메뉴바에 넣고 Frame에 메뉴바 장착
        menuBar.Append(menuFile, 'File')
        self.SetMenuBar(menuBar)
        
        #메뉴에 이벤트(함수) 연결 
        self.Bind(wx.EVT_MENU, self.OnFunc, menuNew)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        self.Move(0,0)
        #self.Center()
        self.Show()
    
    def OnFunc(self, event):
        self.txtA.SetLabelText('새문서')
    
    def OnExit(self, event):
        self.Close(True)
        
if __name__ == '__main__' :
    app = wx.App()
    Example(None, title='메뉴 연습')
    app.MainLoop()
    
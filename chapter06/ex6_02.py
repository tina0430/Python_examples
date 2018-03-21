#버튼과 토글버튼, 이벤트 처리 연습
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(275, 180))
        self.initUI()
        self.Center()
        self.Show()
        
    def initUI(self):
        panel = wx.Panel(self)
        
        #StaticText(메세지 표시용) / TextCtrl(자료 입력용) 컨트롤 배치 ===
        wx.StaticText(panel, label='I D :', pos=(5,5))
        wx.StaticText(panel, label ='PWD :', pos=(5,40))
        self.txtId=wx.TextCtrl(panel, pos=(50,5), size=(200,-1))
        self.txtPwd=wx.TextCtrl(panel, pos=(50,40), size=(200, -1))
        
        #Button 컨트롤 배치 ===
        btn1 = wx.Button(panel, id=1, label='일반버튼', pos=(5,100), size=(70, -1))
        btn1.Bind(wx.EVT_BUTTON, self.onClick)
        
        btn2 = wx.ToggleButton(panel, id=2, label='토글버튼', pos=(90,100), size=(70, -1))
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onClick)
        btn2.id = 2
        
        btn3 = wx.Button(panel, id=3, label='종료', pos=(180,100), size=(70, -1))
        btn3.Bind(wx.EVT_BUTTON, self.onClick)
        btn3.id = 3
        
    def onClick(self, event):
        btnId = event.GetEventObject().Id 
        if btnId == 1:
            dlg = wx.MessageDialog(self, '일반 버튼 처리', '처리', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.txtId.SetLabel('내 아이디는 이거라구(%s)'%self.txtId.GetValue())
            self.txtPwd.SetLabel('내 비밀번호는 이거라구(%s)'%self.txtPwd.GetValue())
        elif btnId == 2:
            #print(event.GetEventObject())   #객체의 주소 출력
            print(event.GetEventObject().GetValue())
            self.SetTitle('토글 연습')
        else:
            self.Close(True)
        
if __name__ =='__main__' :
    app = wx.App()
    MyFrame(None, title='버튼 연습')
    app.MainLoop()
        
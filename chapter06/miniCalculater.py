import wx
import wx.xrc
import operator

class MyFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"미니 계산기", pos = wx.DefaultPosition, size = wx.Size( 315,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        
        self.lblNum1 = wx.StaticText( self.panel1, wx.ID_ANY, u"숫자1 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblNum1.Wrap( -1 )
        bSizer1.Add( self.lblNum1, 0, wx.ALL, 5 )
        
        self.txtNum1 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txtNum1, 0, wx.ALL, 5 )
        
        self.panel1.SetSizer( bSizer1 )
        self.panel1.Layout()
        bSizer1.Fit( self.panel1 )
        bSizer.Add( self.panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.lblNum2 = wx.StaticText( self.panel2, wx.ID_ANY, u"숫자2 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblNum2.Wrap( -1 )
        bSizer2.Add( self.lblNum2, 0, wx.ALL, 5 )
        
        self.txtNum2 = wx.TextCtrl( self.panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNum2, 0, wx.ALL, 5 )
        
        self.panel2.SetSizer( bSizer2 )
        self.panel2.Layout()
        bSizer2.Fit( self.panel2 )
        bSizer.Add( self.panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.lblOpertor = wx.StaticText( self.panel3, wx.ID_ANY, u"연산 선택 :", wx.Point( -1,5 ), wx.DefaultSize, 0 )
        self.lblOpertor.Wrap( -1 )
        bSizer3.Add( self.lblOpertor, 0, wx.ALL, 5 )
        
        radioBoxChoices = [ u"+", u"-", u"*", u"/" ]
        self.radioBox = wx.RadioBox( self.panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, radioBoxChoices, 1, wx.RA_SPECIFY_ROWS )
        self.radioBox.SetSelection( 0 )
        bSizer3.Add( self.radioBox, 0, wx.ALL, 5 )
        
        self.panel3.SetSizer( bSizer3 )
        self.panel3.Layout()
        bSizer3.Fit( self.panel3 )
        bSizer.Add( self.panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.lblResult = wx.StaticText( self.panel4, wx.ID_ANY, u"결과 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblResult.Wrap( -1 )
        bSizer4.Add( self.lblResult, 0, wx.ALL, 5 )
        
        self.lblResultNum = wx.StaticText( self.panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblResultNum.Wrap( -1 )
        bSizer4.Add( self.lblResultNum, 0, wx.ALL, 5 )
        
        
        self.panel4.SetSizer( bSizer4 )
        self.panel4.Layout()
        bSizer4.Fit( self.panel4 )
        bSizer.Add( self.panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.btn1 = wx.Button( self.panel5, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.panel5, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.panel5, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn3, 0, wx.ALL, 5 )
        
        
        self.panel5.SetSizer( bSizer5 )
        self.panel5.Layout()
        bSizer5.Fit( self.panel5 )
        bSizer.Add( self.panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.calculate)
        self.btn2.Bind( wx.EVT_BUTTON, self.reset )
        self.btn3.Bind( wx.EVT_BUTTON, self.exit)
    
    def __del__( self ):
        pass
    
    def isNum(self, num):
        try :
            float(num)
            return True
        except :
            return False
    
    
    def reset( self, event ):   
        self.txtNum1.SetValue('')
        self.txtNum2.SetValue('')
        self.radioBox.SetSelection(0)
    
    def exit( self, event ):
        answer = wx.MessageBox('종료할까요?', '종료', wx.YES_NO)
        if answer == wx.YES:
            self.Close(True)
    
    def calculate( self, event ):
        num1 = self.txtNum1.GetValue()
        num2 = self.txtNum2.GetValue()
        op = self.radioBox.GetSelection()
        ops = {0:'+', 1:'-', 2:'*', 3:'/'}
        opsFunc = {0:operator.add, 1:operator.sub, 2:operator.mul, 3:operator.truediv}
        
        message =''
        
        if self.isNum(num1) and self.isNum(num2):
            if (op == '3' and num2 == '0') :
                wx.MessageBox('0으로 나눌 수 없습니다.', '입력 오류', wx.OK)
                
            else :
                result = str(opsFunc[op](float(num1), float(num2)))
                message = num1 + ops[op]+ num2 + '=' + result
                wx.MessageBox(message, '계산 결과', wx.OK)
                self.lblResultNum.SetLabel(result)
        else :
            wx.MessageBox('숫자만 입력 가능합니다.', '입력 오류', wx.OK)
    
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()
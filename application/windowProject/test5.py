import wx

class MainFrame(wx.Frame):
    panel = None

    def __init__(self):
        super().__init__(None, title="Controls", size=(400, 600))
        self.design()

    def design(self):
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label="**********************다양한 컨트롤(위젯)**********************", pos=(20, 5))

        ##### TextCtrl
        wx.StaticText(self.panel, label="너의 이름은 ", pos=(20, 70))
        self.txtName = wx.TextCtrl(self.panel, value="이름을 입력하세요", pos=(100, 70))
        self.txtName.Bind(wx.EVT_TEXT, self.onText)
        self.txtName.Bind(wx.EVT_KEY_DOWN, self.onKeydown)

        ##### Checkbox
        self.ckMarried = wx.CheckBox(self.panel, label="결혼은?", pos=(20, 120))
        self.ckMarried.Bind(wx.EVT_CHECKBOX, self.onCheck)

        ##### RadioBox
        cboData = ["빨강", "초록", "파랑", "노랑"]
        self.rbColor = wx.RadioBox(self.panel, label="좋아하는 색상은?", pos=(20, 170), choices=cboData)
        self.rbColor.Bind(wx.EVT_RADIOBOX, self.onRadio)

        ##### ComboBox
        self.cboColor = wx.ComboBox(self.panel, pos=(20, 260), choices=cboData)
        self.cboColor.Bind(wx.EVT_COMBOBOX, self.onCombo)

        ##### 결과값 확인
        self.txtShow = wx.TextCtrl(self.panel, pos=(20, 400), size=(320, 150), style=wx.TE_MULTILINE|wx.TE_READONLY)

    def onText(self, e):
        # self.txtShow.AppendText("TextCtrl에서 이벤트 발생 : {}\n".format(self.txtName.GetValue()))
        self.txtShow.AppendText("TextCtrl에서 이벤트 발생 : {}\n".format(e.GetString()))

    def onCheck(self, e):
        self.txtShow.AppendText("CheckBox에서 이벤트 발생 : {}\n".format(e.IsChecked()))

    def onRadio(self, e):
        self.txtShow.AppendText("RadioBox에서 이벤트 발생 : {}, {}\n".format(e.GetInt(), e.GetString()))

    def onCombo(self, e):
        self.txtShow.AppendText("ComboBox에서 이벤트 발생 : {}, {}\n".format(e.GetInt(), e.GetString()))

    def onKeydown(self, e):
        if e.GetKeyCode() == wx.WXK_ESCAPE:
            self.txtName.Clear()

        e.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
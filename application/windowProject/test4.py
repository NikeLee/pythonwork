"""
Dialog(대화 상자)
-------------------------
1. 종류
    1) Built-in Dialog
        - Common Dialog(공통 대화상자)

    2) User Define Dialog

2. 실행 방식
    1) Modal
    2) Modaless
"""


import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="대화 상자", size=(800, 600))
        self.design()

    def design(self):
        menubar = wx.MenuBar()
        menu = wx.Menu()

        item1 = wx.MenuItem(menu, 100, "MessageDialog", "메시지 대화상자 보이기")
        item2 = wx.MenuItem(menu, 101, "ColorDialog", "색상 대화상자 보이기")
        item3 = wx.MenuItem(menu, 102, "FileDialog", "파일 대화상자 보이기")
        item4 = wx.MenuItem(menu, 103, "LoginDialog", "로그인 대화상자 보이기")

        menu.Append(item1)
        menu.Append(item2)
        menu.Append(item3)
        menu.Append(item4)

        menubar.Append(menu, "다이얼로그")
        self.SetMenuBar(menubar)
        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.onMessage, id=100)
        self.Bind(wx.EVT_MENU, self.onColour, id=101)
        self.Bind(wx.EVT_MENU, self.onFile, item3)
        self.Bind(wx.EVT_MENU, self.onLogin, item4)

    def onMessage(self, evt):
        self.SetStatusText("메시지 대화 상자")
        dlg = wx.MessageDialog(self, "오늘 하루도 열심히...", "메시지 박스", wx.OK|wx.ICON_WARNING)

        dlg.ShowModal()

    def onColour(self, evt):
        self.SetStatusText("색상 대화 상자")
        dlg = wx.ColourDialog(self)
        dlg.ShowModal()

    def onFile(self, evt):
        pass

    def onLogin(self, evt):
        pass







if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
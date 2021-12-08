import wx

class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="로그인", size=(300, 200))
        self.design()

    def design(self):
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label="ID :", pos=(10, 5))
        wx.StaticText(self.panel, label="Pass :", pos=(10, 40))

        self.m_id = wx.TextCtrl(self.panel, pos=(60, 5), size=(200, -1))
        self.m_pw = wx.TextCtrl(self.panel, pos=(60, 40))

        btn1 = wx.Button(self.panel, label="로그인", pos=(10, 100))
        btn2 = wx.ToggleButton(self.panel, label="토글 버튼", pos=(100, 100))
        btn3 = wx.Button(self.panel, label="종료", pos=(190, 100))

        btn1.Bind(wx.EVT_BUTTON, self.onHandler)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onHandler)
        btn3.Bind(wx.EVT_BUTTON, self.onHandler)

        btn1.id, btn2.id, btn3.id = 1, 2, 3

    def onHandler(self, evt):
        # print(evt.GetEventObject().id)
        if evt.GetEventObject().id == 1:
            id = self.m_id.GetValue()
            pw = self.m_pw.GetValue()

            if id == "tiger" and pw == "1111":
                msg = "로그인이 되었습니다."
            else:
                msg = "로그인이 거부되었습니다."

            wx.MessageDialog(self, msg, "로그인", wx.OK).ShowModal()
        elif evt.GetEventObject().id == 2:
            if evt.GetEventObject().GetValue():
                self.panel.SetBackgroundColour((wx.Colour(255, 0, 0)))
                self.panel.Refresh()
            else:
                self.panel.SetBackgroundColour((wx.Colour(255, 255, 255)))
                self.panel.Refresh()
        else:
            self.Close(True)

    # def onBtn1(self, evt):
    #     id = self.m_id.GetValue()
    #     pw = self.m_pw.GetValue()
    #
    #     if id == "tiger" and pw == "1111":
    #         msg = "로그인이 되었습니다."
    #     else:
    #         msg = "로그인이 거부되었습니다."
    #
    #     wx.MessageDialog(self, msg, "로그인", wx.OK).ShowModal()
    #
    # def onBtn2(self, evt):
    #     # print(evt.GetEventObject())
    #     # print(evt.GetEventObject().GetValue())
    #     if evt.GetEventObject().GetValue():
    #         self.panel.SetBackgroundColour((wx.Colour(255, 0, 0)))
    #         self.panel.Refresh()
    #     else:
    #         self.panel.SetBackgroundColour((wx.Colour(255, 255, 255)))
    #         self.panel.Refresh()
    #
    # def onBtn3(self, evt):
    #     self.Close(True)









if __name__ == "__main__":
    app = wx.App()
    frame = LoginFrame()
    frame.Show(True)
    app.MainLoop()
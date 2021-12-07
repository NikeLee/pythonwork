import wx

class MemoFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="메모장 프로그램")
        self.design()

    def design(self):
        # 메뉴 : 고정식 메뉴(pull down), 이동식 메뉴(pop up)
        # MenuBar, Menu, MenuItem
        menubar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuEdit = wx.Menu()

        mnuFile_new = wx.MenuItem(mnuFile, wx.ID_NEW, "New", "New Document")
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, "Open", "파일 열기")
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, "Exit", "프로그램 종료")

        mnuFile.Append(mnuFile_new)
        mnuFile.Append(mnuFile_open)
        mnuFile.Append(mnuFile_exit)

        menubar.Append(mnuFile, "파일")
        menubar.Append(mnuEdit, "편집")

        self.SetMenuBar(menubar)

        wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()

        #self.Move(100, 100)
        self.Center()


if __name__ == "__main__":
    app = wx.App()
    frame = MemoFrame()
    frame.Show(True)
    app.MainLoop()

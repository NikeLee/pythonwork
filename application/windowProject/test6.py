"""
Layout
========
Sizer 클래스
    - wx.BoxSizer : 가로 또는 세로로 컨트롤을 배치
    - wx.GridSizer : 그리드와 같은 구조로 컨트롤을 배치
    - wx.FlexGridSizer

wxFormBuilder
----------------
http://sourceforge.net
"""

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Sizer", size=(400, 600))

        panel1 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel1.SetBackgroundColour("BLUE")

        panel2 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel2.SetBackgroundColour("RED")

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 3, wx.EXPAND)
        box.Add(panel2, 1, wx.EXPAND)

        self.SetSizer(box)




if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
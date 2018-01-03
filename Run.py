import os
import wx
from libs.ui.Client import Client
import libs.Logger

if __name__ == '__main__':
    app = wx.App()
    app.TopWindow = Client()
    app.TopWindow.Show()
    app.MainLoop()

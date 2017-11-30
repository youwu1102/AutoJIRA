import os
import wx
from libs.ui.Client import Client


if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()

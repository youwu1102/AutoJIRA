from libs.ui.Client import Client
from libs.ui.LoginDialog import Login
import wx


if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()

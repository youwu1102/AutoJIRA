from libs.ui.Client import Client
import wx


if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()

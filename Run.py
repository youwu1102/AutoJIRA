import os
hostname = os.environ['COMPUTERNAME']
if hostname == 'APT-GFX-SH002':
    from libs.ui.Client import Client
else:
    from libs.ui.ClientSimplify import Client
import wx


if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()

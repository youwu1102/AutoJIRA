# -*- encoding:UTF-8 -*-
import wx
import threading
import urllib2
from base64 import encodestring
"""
Author：You Wu

"""


class LoginDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, title="QC Login", size=(280, 230))
        self.Center()
        self.__init_ui()

    def __init_ui(self):
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, pos=(15, 18), label="Account:")
        wx.StaticText(panel, -1, pos=(15, 58), label="Password:")
        self.account_input = wx.TextCtrl(panel, -1, pos=(85, 15), size=(170, -1))
        self.password_input = wx.TextCtrl(panel, -1, pos=(85, 55), size=(170, -1), style=wx.TE_PASSWORD)
        #self.remember_me_checkbox = wx.CheckBox(panel, -1, label='Remember Me', pos=(30, 90))
        self.remember_me_checkbox = wx.CheckBox(panel, -1, label='Useless   A', pos=(30, 90))
        #self.auto_login_checkbox = wx.CheckBox(panel, -1, label='Auto Login', pos=(160, 90))
        self.auto_login_checkbox = wx.CheckBox(panel, -1, label='Useless  B', pos=(160, 90))
        login_button = wx.Button(panel, wx.ID_OK, label='Login', pos=(40, 120), size=(90, -1))
        wx.Button(panel, wx.ID_CANCEL, label='Cancel', pos=(150, 120), size=(90, -1))
        self.info_text = wx.StaticText(panel, -1, pos=(0, 160), size=(-1, -1))
        self.Bind(wx.EVT_BUTTON, self.__on_login, login_button)



    def __check_auto_login(self, event):
        pass

    def __check_remember_me(self, event):
        pass

    def __on_login(self, event):
        account = self.account_input.GetValue()
        password = self.password_input.GetValue()
        if not account or not password:
            self.refresh_info_text(text='Please input account or password', type='E')
        else:
            self.authorization(account, password)


    def authorization(self, account, password):
        request = urllib2.Request('https://jira-cstm-tools.qualcomm.com/jira/')
        request.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (account,password))[:-1])
        try:
            urllib2.urlopen(request)
            self.refresh_info_text('                         Success.                         ', 'I')
            self.Destroy()
        except urllib2.HTTPError:
            self.refresh_info_text('Authorization Fail: Account or Password is incorrect.', 'E')
        except urllib2.URLError:
            self.refresh_info_text('Connection Fail: Please check whether JIRA can visit normally.', 'E')



    def refresh_info_text(self, text, type):
        self.info_text.Label = text

if __name__ == '__main__':
    app = wx.App()
    login = LoginDialog()
    login.Show()
    app.MainLoop()
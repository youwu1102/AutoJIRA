# -*- encoding:UTF-8 -*-
import wx

"""
Author：You Wu

"""


class Login(wx.Dialog):
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
        self.remember_me_checkbox = wx.CheckBox(panel, -1, label='Remember Me', pos=(30, 90))
        self.auto_login_checkbox = wx.CheckBox(panel, -1, label='Auto Login', pos=(160, 90))
        login_button = wx.Button(panel, -1, label='Login', pos=(40, 120), size=(90, -1))
        cancel_button = wx.Button(panel, -1, label='Cancel', pos=(150, 120), size=(90, -1))
        self.info_text = wx.StaticText(panel, -1, pos=(20,150), size=(170, -1))
        self.Bind(wx.EVT_BUTTON, self.__on_login, login_button)
        self.Bind(wx.EVT_BUTTON, self.__on_cancel, cancel_button)


    def __check_auto_login(self, event):
        print self.account_input.GetValue()
        print self.password_input.GetValue()
        pass

    def __check_remember_me(self, event):
        pass

    def __on_login(self, event):
        print self.account_input.GetValue()
        print self.password_input.GetValue()

    def __on_cancel(self, event):
        self.Destroy()




if __name__ == '__main__':
    app = wx.App()
    login = Login()
    login.Show()
    app.MainLoop()
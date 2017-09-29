# -*- encoding:UTF-8 -*-
import wx
from libs import GlobalVariable, JIRA


class LoginDialog(wx.Dialog):
    def __init__(self, thread_manager):
        wx.Dialog.__init__(self, None, -1, title="QC Login", size=(280, 230))
        self.Center()
        self.__init_ui()
        self.__thread_manager = thread_manager

    def __init_ui(self):
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, pos=(15, 18), label="Account:")
        wx.StaticText(panel, -1, pos=(15, 58), label="Password:")
        self.account_input = wx.TextCtrl(panel, -1, pos=(85, 15), size=(170, -1))
        self.password_input = wx.TextCtrl(panel, -1, pos=(85, 55), size=(170, -1), style=wx.TE_PASSWORD)
        #self.remember_me_checkbox = wx.CheckBox(panel, -1, label='Remember Me', pos=(30, 90))
        #self.remember_me_checkbox = wx.CheckBox(panel, -1, label='Useless   A', pos=(30, 90))
        #self.auto_login_checkbox = wx.CheckBox(panel, -1, label='Auto Login', pos=(160, 90))
        #self.auto_login_checkbox = wx.CheckBox(panel, -1, label='Useless  B', pos=(160, 90))
        login_button = wx.Button(panel, wx.ID_OK, label='Login', pos=(40, 120), size=(90, -1))
        wx.Button(panel, wx.ID_CANCEL, label='Cancel', pos=(150, 120), size=(90, -1))
        self.info_text = wx.StaticText(panel, -1, pos=(0, 160), size=(280, -1), style=wx.ALIGN_CENTRE)
        self.Bind(wx.EVT_BUTTON, self.__on_login, login_button)
        self.account_input.SetValue(GlobalVariable.account)
        self.password_input.SetValue(GlobalVariable.password)


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
            GlobalVariable.account = account
            GlobalVariable.password = password
            state, response, error = JIRA.authorization(account=account, password=password)
            if state == 0:
                self.refresh_info_text('Success.', 'I')
                self.Destroy()
            elif state == 1:
                self.refresh_info_text('Account or Password is incorrect.', 'E')
            elif state == 2:
                self.refresh_info_text('Please check whether JIRA can visit normally.', 'E')

    def refresh_info_text(self, text, type):
        self.info_text.Label = text

if __name__ == '__main__':
    app = wx.App()
    login = LoginDialog()
    login.Show()
    app.MainLoop()
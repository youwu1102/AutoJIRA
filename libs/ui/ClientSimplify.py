# -*- encoding:UTF-8 -*-
from libs.ui.zLoginDialog import LoginDialog
from libs.ui.zCreateIssueDialog import CreateIssueDialog
from libs.ui.zBatchSubmitIssueDialog import BatchSubmitIssueDialog
from libs.ui.GridData import GridData
import wx
import wx.grid
import wx.lib.agw.customtreectrl as CT
# from wx.calendar import CalendarCtrl
# CalendarCtrl(self.panel)


class Client(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title="JIRA", size=(200, 200))
        self.Center()
        self.panel = wx.Panel(self, -1)
        create_issue_button = wx.Button(self.panel, -1, 'Create Issue', pos=(50, 30), size=(100, -1))
        batch_submission_button = wx.Button(self.panel, -1, 'Batch Sub', pos=(50, 80), size=(100, -1))
        self.Bind(wx.EVT_BUTTON, self.__create_issue, create_issue_button)
        self.Bind(wx.EVT_BUTTON, self.__batch_submission, batch_submission_button)
        self.__open_login()

    def __open_login(self):
        login = LoginDialog()
        result = login.ShowModal()
        if result == wx.ID_CANCEL:
            login.Destroy()
            self.Destroy()

    def __create_issue(self, event):
        issue = CreateIssueDialog()
        if issue.ShowModal() == wx.ID_CANCEL:
            issue.Destroy()

    def __batch_submission(self, event):
        issue_list = list()
        dlg = wx.FileDialog(self,
                            message="Select Template",
                            wildcard="Issue Template (*.xml)|*.xml|All files (*.*)|*.*",
                            defaultDir='C:\Users\c_youwu\Documents\GitHub\JIRA_FOR_CHNAPSS\\resource\\template',
                            style=wx.OPEN|wx.FD_MULTIPLE
                            )
        if dlg.ShowModal() == wx.ID_OK:
            issue_list = dlg.GetPaths()
        dlg.Destroy()
        if issue_list:
            dialog = BatchSubmitIssueDialog(issue_list)
            dialog.ShowModal()
            dialog.Destroy()


if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    client.Destroy()
    app.MainLoop()

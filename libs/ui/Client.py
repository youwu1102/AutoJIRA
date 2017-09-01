# -*- encoding:UTF-8 -*-
from libs.ui.LoginDialog import LoginDialog
from libs.ui.zCreateIssueDialog import CreateIssueDialog
import wx
import wx.grid
import wx.lib.agw.customtreectrl as CT
# from wx.calendar import CalendarCtrl
# CalendarCtrl(self.panel)
"""
Author：You Wu

"""

class Client(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title="jira-cstm.qualcomm.com", size=(1000, 600))
        self.Center()
        self.panel = wx.Panel(self, -1)
        main_box = wx.BoxSizer(wx.VERTICAL)  # 容纳其他所有容器的box
        toolbar_box = self.__init_tool_box()
        tree_and_grid_box = self.__init_grid_and_tree_box()
        main_box.Add(toolbar_box, 1, wx.EXPAND)
        main_box.Add(tree_and_grid_box, 7, wx.EXPAND)
        self.panel.SetSizer(main_box)
        #self.__open_login()

    def __open_login(self):
        login = LoginDialog()
        result = login.ShowModal()
        if result == wx.ID_CANCEL:
            login.Destroy()
            self.Destroy()
        del login

    def __init_tool_box(self):
        toolbar_box = wx.BoxSizer(wx.HORIZONTAL)  # 工具栏
        create_issue_button = wx.Button(self.panel, -1, 'Create Issue', size=(-1, -1))
        batch_submission_button = wx.Button(self.panel, -1, 'Batch Sub', size=(-1, -1))
        self.Bind(wx.EVT_BUTTON, self.__create_issue, create_issue_button)
        self.Bind(wx.EVT_BUTTON, self.__batch_submission, batch_submission_button)
        toolbar_box.Add(create_issue_button)
        toolbar_box.Add(batch_submission_button)
        return toolbar_box

    def __init_grid_and_tree_box(self):
        def init_grid(panel):
            grid = wx.grid.Grid(panel, -1)
            return grid

        def init_tree(panel):
            tree_box = wx.BoxSizer(wx.VERTICAL)
            title = wx.StaticText(panel, -1, "Query")

            tree = CT.CustomTreeCtrl(panel, agwStyle=wx.TR_DEFAULT_STYLE|CT.TR_AUTO_CHECK_PARENT|CT.TR_AUTO_CHECK_CHILD)
            tree_box.Add(title)
            tree_box.Add(tree)
            return tree_box

        tree_and_grid_box = wx.BoxSizer(wx.HORIZONTAL)
        grid_module = init_grid(self.panel)
        tree_module = init_tree(self.panel)  # 树状查询
        tree_and_grid_box.Add(tree_module, 1, wx.EXPAND)
        tree_and_grid_box.Add(grid_module, 8, wx.EXPAND)
        return tree_and_grid_box

    def __create_issue(self, event):
        issue = CreateIssueDialog()
        issue.ShowModal()

    def __batch_submission(self, event):
        dlg = wx.FileDialog(self,
                            message="Select Template",
                            wildcard="Issue Template (*.xml)|*.xml|All files (*.*)|*.*",
                            defaultDir='C:\Git\AppStress\\repository\cases\ChinaAppStress\\3rd_party_random\com.baidu.appsearch',
                            style=wx.OPEN|wx.FD_MULTIPLE
                            )
        if dlg.ShowModal() == wx.ID_OK:
            profile_path = dlg.GetPaths()
            for a in profile_path:
                print a
            # profile = Utility.parse_profile(profile_path=profile_path)
            # self.__change_options_from_profile(profile)
        dlg.Destroy()



if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()

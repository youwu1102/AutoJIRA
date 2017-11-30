# -*- encoding:UTF-8 -*-
from libs.ui.zLoginDialog import LoginDialog
from libs.ui.zProgressDialog import ProgressDialog
from libs.ui.zCreateIssueDialog import CreateIssueDialog
from libs.ui.zBatchSubmitIssueDialog import BatchSubmitIssueDialog
from libs import Utility
from os import listdir
from libs.ui.GridData import GridData
from libs import GlobalVariable
import wx
from wx.grid import Grid
from wx import grid
from libs.ThreadManager import ThreadManager


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
        self.grid_data = GridData()
        main_box = wx.BoxSizer(wx.VERTICAL)  # 容纳其他所有容器的box
        toolbar_box = self.__init_tool_box()
        tree_and_grid_box = self.__init_grid_and_tree_box()
        main_box.Add(toolbar_box, 1, wx.EXPAND)
        main_box.Add(tree_and_grid_box, 7, wx.EXPAND)
        self.panel.SetSizer(main_box)
        self.thread_manager = ThreadManager(data=self.grid_data, update=self.__update_grid)
        self.thread_manager.setDaemon(True)
        self.thread_manager.start()
        self.__open_login()


    def __open_login(self):
        login = LoginDialog(self.thread_manager)
        result = login.ShowModal()
        if result == wx.ID_CANCEL:
            login.Destroy()
            self.Destroy()

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
            grid_box = wx.BoxSizer(wx.VERTICAL)
            title = wx.StaticText(panel, -1, "Grid")
            data_grid = Grid(panel, -1, size=(700, -1))
            data_grid.SetTable(self.grid_data)
            data_grid.AdjustScrollbars()
            data_grid.EnableEditing(False)   # 设置数据无法修改
            data_grid.SetRowLabelSize(40)
            data_grid.SetColLabelSize(20)
            data_grid.DisableDragRowSize()  # 设置无法拖动修改行高
            data_grid.SetSelectionMode(Grid.wxGridSelectRows)  # 设置整行选取模式
            data_grid.Refresh()
            data_grid.Bind(grid.EVT_GRID_CELL_RIGHT_DCLICK, self.copy_line)
            button_box = wx.BoxSizer(wx.HORIZONTAL)
            previous_button = wx.Button(panel, -1, '<', size=(-1, -1))
            next_button = wx.Button(panel, -1, '>', size=(-1, -1))
            self.Bind(wx.EVT_BUTTON, self.__on_previous, previous_button)
            self.Bind(wx.EVT_BUTTON, self.__on_next, next_button)
            button_box.Add(previous_button)
            button_box.Add(next_button)
            grid_box.Add(title,0)
            grid_box.Add(data_grid, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.BOTTOM, 5)
            grid_box.Add(button_box, 0,  wx.EXPAND | wx.BOTTOM, 5)
            return data_grid, grid_box

        def init_tree(panel):
            tree_box = wx.BoxSizer(wx.VERTICAL)
            title = wx.StaticText(panel, -1, "Query")
            tree = wx.TreeCtrl(panel,style=wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT|wx.TR_LINES_AT_ROOT)
            root = tree.AddRoot('Root')
            queries = listdir(GlobalVariable.query_folder)
            for query in queries:
                if query.endswith('.xml'):
                    Utility.append_tree(tree=tree, root=root, query=Utility.path_join(GlobalVariable.query_folder, query))
            tree_box.Add(title)
            tree_box.Add(tree, 1, wx.EXPAND | wx.ALL, 5)
            self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.__right_click_on_tree)

            return tree, tree_box

        tree_and_grid_box = wx.BoxSizer(wx.HORIZONTAL)
        self.grid, grid_module = init_grid(self.panel)
        self.tree, tree_module = init_tree(self.panel)  # 树状查询
        tree_and_grid_box.Add(tree_module, 3, wx.EXPAND)
        tree_and_grid_box.Add(grid_module, 7, wx.EXPAND)
        return tree_and_grid_box

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

    def copy_line(self, event):
        # 没有把列的TITLE罗列出来 需要优化
        rows = self.grid.GetSelectedRows()
        rows.sort()
        print rows
        string = ''
        for row in rows:
            row_string = ''
            for col in range(self.grid.GetNumberCols()):
                value = self.grid.GetCellValue(row, col)
                if '\r' in value or '\n' in value:
                    value = '\"%s\"' % value
                row_string += '%s\t' % value
            string = string + row_string.rstrip('\t') + '\n'
        Utility.send_to_clipboard(string.rstrip('\n'))

    def __right_click_on_tree(self, event):
        menu = wx.Menu()
        menu.Append(1, 'Query')
        #menu.Append(2, 'Hello')
        self.Bind(wx.EVT_MENU, self.__query, id=1)
        self.Bind(wx.EVT_MENU, self.__hello, id=2)
        self.PopupMenu(menu, event.GetPoint())
        menu.Destroy()

    def __query(self, event):
        def get_query_name(node):
            p = self.tree.GetItemParent(node)
            if p == self.tree.RootItem:
                return self.tree.GetItemText(node)
            return get_query_name(p)
        query_name = get_query_name(self.tree.Selection)
        query_string = Utility.convert_to_string(GlobalVariable.dict_query_config.get(query_name))
        dialog = ProgressDialog(seconds=3, title='Query', message='Querying...')
        self.thread_manager.append_work(query=query_string, type='query', start=0, dialog=dialog)
        dialog.ShowModal()

    def __hello(self, event):
        print 'Hello'

    def __update_grid(self):
        self._store_grid_cols_width()
        self.grid_data.reset_cols(list('abcd'))
        self.grid.SetTable(self.grid_data)
        self.grid.SetSelectionMode(Grid.wxGridSelectRows)  # 设置整行选取模式
        self.grid.Refresh()

    def _store_grid_cols_width(self):
        tmp = list()
        for x in range(self.grid_data.GetNumberCols()):
            tmp.append(self.grid.GetColSize(x))
        return tmp

    def __on_previous(self, event):
        self.thread_manager.append_work(type='previous')

    def __on_next(self, event):
        dialog = ProgressDialog(seconds=3, title='Query', message='Querying...')
        self.thread_manager.append_work(type='next', dialog=dialog)
        dialog.ShowModal()




if __name__ == '__main__':
    app = wx.App()
    client = Client()
    client.Show()
    app.MainLoop()

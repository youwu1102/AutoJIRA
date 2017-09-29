# -*- coding: utf-8 -*-
import wx
import yIssueFromXML
from libs import Utility, JIRA, GlobalVariable
import webbrowser
import threading
from wx import CallAfter
from os.path import sep

class BatchSubmitIssueDialog(wx.Dialog):
    def __init__(self, issue_list):
        wx.Dialog.__init__(self, None, -1, title="Batch Submit Issue", size=(300, 460))
        self.Center()
        self.issue_list = issue_list
        self.submit_result = dict()
        self.__init_ui()

    def __init_ui(self):
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, pos=(0, 2), label='Submit Result', size=(293, -1), style=wx.ALIGN_CENTER)
        self.submit_result_list_box = wx.ListBox(panel, -1, pos=(0, 20), size=(293, 300), choices=[], style=wx.LB_HSCROLL | wx.LB_EXTENDED)
        self.submit_result_list_box.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.LIGHT))
        self.info_text = wx.StaticText(panel, -1, pos=(0, 400), label='', size=(293, 50), style=wx.ALIGN_CENTER)
        self.info_text.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD))
        self.done_button = wx.Button(panel, wx.ID_OK, label='DONE', pos=(0, 350), size=(293, 30))
        self.done_button.Disable()
        open_button = wx.Button(panel, -1, label='Open In Browser', pos=(0, 320), size=(146, 30))
        export_button = wx.Button(panel, -1, label='Export To Excel', pos=(147, 320), size=(146, 30))
        self.Bind(wx.EVT_BUTTON, self.open_in_browser, open_button)
        self.Bind(wx.EVT_BUTTON, self.export_to_excel, export_button)
        thread = sumbit_jira(issue_list=self.issue_list, dialog=self)
        thread.setDaemon(True)
        thread.start()

    def open_in_browser(self, event):
        selected_list = self.submit_result_list_box.GetSelections()
        for selected in selected_list:
            string = self.submit_result_list_box.GetString(selected)
            s_list = string.split('|')
            jira_id = self.submit_result.get(s_list[1]).get('jira_id')
            if jira_id:
                webbrowser.open(url='https://jira-cstm.qualcomm.com/jira/browse/%s' % jira_id, new=0, autoraise=True)

    def export_to_excel(self, event):
        print 'Not Ready'

    def refresh_info(self, msg):
        self.info_text.SetLabel(msg)

    def append_result(self, result):
        self.submit_result_list_box.Append(result)

    def enable_done(self):
        self.done_button.Enable()



class sumbit_jira(threading.Thread):
    def __init__(self, issue_list, dialog):
        threading.Thread.__init__(self)
        self.issue_list = issue_list
        self.dialog = dialog
        self.refresh = dialog.refresh_info
        self.append = dialog.append_result
        self.enable = dialog.enable_done
        self.thread_stop = False

    def run(self):
        for issue_path in self.issue_list:
            file_name = issue_path.split(sep)[-1]
            self.refresh_info('Current: %5d      Total: %5d' % (self.issue_list.index(issue_path)+1, len(self.issue_list)))
            if self.thread_stop or not self.dialog:
                break
            issue_dict = Utility.parse_profile(issue_path)
            issue = yIssueFromXML.generate(issue_dict=issue_dict)
            state, response, error = JIRA.create(data=issue, account='qrd_automation', password='1234Abcd')
            issue_dict['state'] = state
            issue_dict['response'] = response
            issue_dict['error'] = error

            if state == 0:
                response = eval(response)
                jira_id = response.get("key")
                issue_dict['jira_id'] = jira_id
                self.append_result('%-14s|%s' % (jira_id, file_name))
            else:
                self.append_result('%-14s|%s' % ('Submit Fail', file_name))
            self.updata_result(key=file_name, value=issue_dict)
        self.enable_done()

    def stop(self):
        self.thread_stop = True

    def refresh_info(self, msg):
        if self.dialog:
            CallAfter(self.refresh, msg)

    def append_result(self, result):
        if self.dialog:
            CallAfter(self.append, result)

    def enable_done(self):
        if self.dialog:
            CallAfter(self.enable, )

    def updata_result(self, key, value):
        if self.dialog:
            self.dialog.submit_result[key] = value

if __name__ == '__main__':
    import time
    app = wx.App()
    print time.time()
    dialog = BatchSubmitIssueDialog(list('abcedfghijlkm'))
    dialog.ShowModal()
    dialog.Destroy()
    print time.time()
    app.MainLoop()
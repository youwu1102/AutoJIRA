# -*- encoding:UTF-8 -*-
import wx
import IssueConfiguration as ic

"""
Author：You Wu

"""


class IssueDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, title="Create Issue", size=(745, 775))
        self.Center()
        self.__init_ui()

    def __static_text(self, pos, label):
        x, y = pos
        if label[-1] != '*':
            label += ' '
        wx.StaticText(self.panel, -1, pos=(x+3, y+3), label=label, style=wx.ALIGN_RIGHT, size=(105, -1))

    def __init_ui(self):
        self.panel = wx.Panel(self)
        height1 = 20
        height2 = height1 + 30
        height3 = height2 + 30
        height4 = height3 + 30
        height5 = height4 + 30
        height6 = height5 + 30
        height7 = height6 + 30
        height8 = height7 + 30
        height9 = height8 + 30
        height10 = height9 + 305
        height11 = height10 + 30
        height12 = height11 + 30
        height13 = height12 + 30
        height14 = height13 + 30
        height15 = height14 + 37
        static_text_width = 105
        x_gap = 5
        width1 = 15
        width2 = width1 + static_text_width + x_gap
        width3 = width2 + 120 + x_gap
        width4 = width3 + static_text_width + x_gap
        width5 = width4 + 120 + x_gap
        width6 = width5 + static_text_width + x_gap
        width7 = width2 + 235 + x_gap
        width8 = width7 + static_text_width + x_gap

        self.__static_text(pos=(width1, height1), label='Project*')
        self.project_choice = wx.Choice(self.panel, -1, pos=(width2, height1), choices=ic.project.get(ic.choice), size=(120, -1))
        self.project_choice.SetStringSelection(ic.project.get(ic.default))
        self.project_choice.Disable()

        self.__static_text(pos=(width3, height1), label='Issue Type*')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height1), choices=ic.issue_type.get(ic.choice), size=(120, -1))
        self.issue_type_choice.SetStringSelection(ic.issue_type.get(ic.default))
        self.issue_type_choice.Disable()


        self.__static_text(pos=(width5, height1), label='Crash*')
        self.crash_choice = wx.Choice(self.panel, -1, pos=(width6, height1), choices=ic.crash.get(ic.choice), size=(120, -1))
        self.crash_choice.SetStringSelection(ic.crash.get(ic.default))

        self.__static_text(pos=(width1, height2), label='Repeatability*')
        self.repeatability_choice = wx.Choice(self.panel, -1, pos=(width2, height2), choices=ic.repeatability.get(ic.choice), size=(120, -1))
        self.repeatability_choice.SetStringSelection(ic.repeatability.get(ic.default))

        self.__static_text(pos=(width3, height2), label='Severity*')
        self.severity_choice = wx.Choice(self.panel, -1, pos=(width4, height2), choices=ic.severity.get(ic.choice), size=(120, -1))
        self.repeatability_choice.SetStringSelection(ic.severity.get(ic.default))

        self.__static_text(pos=(width5, height2), label='Component/s*')
        self.component = wx.CheckListBox(self.panel, -1, pos=(width6, height2), choices=ic.severity.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width1, height3), label='Product Name*')
        self.project_choice = wx.Choice(self.panel, -1, pos=(width2, height3), choices=['1'], size=(120, -1))
        self.__static_text(pos=(width3, height3), label='Test Group*')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height3), choices=['2'], size=(120, -1))
        self.__static_text(pos=(width5, height3), label='Test Phase*')
        self.crash_choice = wx.Choice(self.panel, -1, pos=(width6, height3), choices=['3'], size=(120, -1))

        self.__static_text(pos=(width1, height4), label='Area')
        self.project_choice = wx.Choice(self.panel, -1, pos=(width2, height4), choices=['1'], size=(120, -1))
        self.__static_text(pos=(width3, height4), label='LA Functionality')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height4), choices=['2'], size=(120, -1))
        self.__static_text(pos=(width5, height4), label='MM Functionality')
        self.crash_choice = wx.Choice(self.panel, -1, pos=(width6, height4), choices=['3'], size=(120, -1))

        self.__static_text(pos=(width1, height5), label='UI Functionality')
        self.project_choice = wx.Choice(self.panel, -1, pos=(width2, height5), choices=['1'], size=(120, -1))
        self.__static_text(pos=(width3, height5), label='CNSS Functionality')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height5), choices=['2'], size=(120, -1))
        self.__static_text(pos=(width5, height5), label='BSP Functionality')
        self.crash_choice = wx.Choice(self.panel, -1, pos=(width6, height5), choices=['3'], size=(120, -1))

        self.__static_text(pos=(width1, height6), label='Assignee')
        self.project_choice = wx.Choice(self.panel, -1, pos=(width2, height6), choices=['1'], size=(120, -1))
        self.__static_text(pos=(width3, height6), label='Customer Name')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height6), choices=['2'], size=(120, -1))
        self.__static_text(pos=(width5, height6), label='Labels')
        self.crash_choice = wx.Choice(self.panel, -1, pos=(width6, height6), choices=['3'], size=(120, -1))

        self.__static_text(pos=(width1, height7), label='Sprint')
        self.project_choice = wx.Choice(self.panel, -1, pos=(width2, height7), choices=['1'], size=(120, -1))
        self.__static_text(pos=(width3, height7), label='Category Type')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height7), choices=['2'], size=(120, -1))

        self.__static_text(pos=(width1, height8), label='Summary*')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width2, height8), size=(590, -1))
        self.__static_text(pos=(width1, height9), label='Description*')
        self.description_input = wx.TextCtrl(self.panel, -1, pos=(width2, height9), size=(590, 300), style=wx.TE_MULTILINE)
        self.__static_text(pos=(width1, height10), label='Log link*')
        self.log_link_input = wx.TextCtrl(self.panel, -1, pos=(width2, height10), size=(590, -1))


        self.__static_text(pos=(width1, height11), label='SR Number')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width2, height11), size=(240, -1))
        self.__static_text(pos=(width7, height11), label='External JIRA ID')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width8, height11), size=(240, -1))

        self.__static_text(pos=(width1, height12), label='Serial Number')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width2, height12), size=(240, -1))
        self.__static_text(pos=(width7, height12), label='MCN number')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width8, height12), size=(240, -1))
        self.__static_text(pos=(width1, height13), label='MetaBuildLocation')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width2, height13), size=(590, -1))

        create_button = wx.Button(self.panel, -1, label='Create', pos=(550, height14), size=(80, 30))
        cancel_button = wx.Button(self.panel, wx.ID_CANCEL, label='Cancel', pos=(635, height14), size=(80, 30))
        self.auto_login_checkbox = wx.CheckBox(self.panel, -1, label='Save Current As The Default', pos=(550, height15))

        wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=wx.Bitmap("C:\Users\c_youwu\PycharmProjects\AutoJIRA\\resource\icon\import.png", wx.BITMAP_TYPE_PNG), pos=(width1 + 18, height14 + 8), size=(34, 34))
        wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=wx.Bitmap("C:\Users\c_youwu\PycharmProjects\AutoJIRA\\resource\icon\export.png", wx.BITMAP_TYPE_PNG), pos=(width1 + 52, height14 + 8), size=(34, 34))

if __name__ == '__main__':
    import time
    print time.time()
    app = wx.App()
    login = IssueDialog()
    print time.time()
    login.Show()
    print time.time()
    app.MainLoop()
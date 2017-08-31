import wx
import IssueConfiguration as ic
import Issue
from libs.JIRA import JIRA
from os.path import exists
import libs.Utility

class IssueDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, title="Create Issue", size=(745, 775))
        self.Center()
        default_profile = 'Default.xml'
        self.__init_ui()
        self.__change_options(default_profile)

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
        height14 = height13 + 40

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
        self.project_choice.Disable()

        self.__static_text(pos=(width3, height1), label='Issue Type*')
        self.issue_type_choice = wx.Choice(self.panel, -1, pos=(width4, height1), choices=ic.issue_type.get(ic.choice), size=(120, -1))
        self.issue_type_choice.Disable()

        self.__static_text(pos=(width5, height1), label='Crash*')
        self.crash_choice = wx.Choice(self.panel, -1, pos=(width6, height1), choices=ic.crash.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width1, height2), label='Repeatability*')
        self.repeatability_choice = wx.Choice(self.panel, -1, pos=(width2, height2), choices=ic.repeatability.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width3, height2), label='Severity*')
        self.severity_choice = wx.Choice(self.panel, -1, pos=(width4, height2), choices=ic.severity.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width5, height2), label='Component/s*')
        self.component_input = wx.TextCtrl(self.panel, -1, pos=(width6, height2), size=(100, 24), style=wx.TE_READONLY)
        component_button = wx.Button(self.panel, -1, label='...', pos=(width6+100, height2-1), size=(20, 26))
        self.Bind(wx.EVT_BUTTON, self.on_components, component_button)

        self.__static_text(pos=(width1, height3), label='Product Name*')
        self.product_name_choice = wx.Choice(self.panel, -1, pos=(width2, height3), choices=ic.product_name.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width3, height3), label='Test Group*')
        self.test_group_choice = wx.Choice(self.panel, -1, pos=(width4, height3), choices=ic.test_group.get(ic.choice), size=(120, -1))


        self.__static_text(pos=(width5, height3), label='Test Phase*')
        self.test_phase_choice = wx.Choice(self.panel, -1, pos=(width6, height3), choices=ic.test_phase.get(ic.choice), size=(120, -1))


        self.__static_text(pos=(width1, height4), label='Area')
        self.area_choice = wx.Choice(self.panel, -1, pos=(width2, height4), choices=ic.area.get(ic.choice), size=(120, -1))


        self.__static_text(pos=(width3, height4), label='LA Functionality')
        self.la_functionality_choice = wx.Choice(self.panel, -1, pos=(width4, height4), choices=ic.la_functionality.get(ic.choice), size=(120, -1), style=wx.LB_HSCROLL)


        self.__static_text(pos=(width5, height4), label='MM Functionality')
        self.mm_functionality_choice = wx.Choice(self.panel, -1, pos=(width6, height4), choices=ic.mm_functionality.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width1, height5), label='UI Functionality')
        self.ui_functionality_choice = wx.Choice(self.panel, -1, pos=(width2, height5), choices=ic.ui_functionality.get(ic.choice), size=(120, -1))


        self.__static_text(pos=(width3, height5), label='CNSS Functionality')
        self.cnss_functionality_choice = wx.Choice(self.panel, -1, pos=(width4, height5), choices=ic.cnss_functionality.get(ic.choice), size=(120, -1))


        self.__static_text(pos=(width5, height5), label='BSP Functionality')
        self.bsp_functionality_choice = wx.Choice(self.panel, -1, pos=(width6, height5), choices=ic.bsp_functionality.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width1, height6), label='Assignee')
        self.assignee_input = wx.TextCtrl(self.panel, -1, pos=(width2, height6), size=(100, 24), style=wx.TE_READONLY)

        assignee_button = wx.Button(self.panel, -1, label='...', pos=(width2+100, height6-1), size=(20, 26))
        assignee_button.Disable()
        self.Bind(wx.EVT_BUTTON, self.on_assignee, assignee_button)
        # complete here

        self.__static_text(pos=(width3, height6), label='Customer Name')
        self.customer_name_choice = wx.Choice(self.panel, -1, pos=(width4, height6), choices=ic.customer_name.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width5, height6), label='Labels')
        self.labels_choice = wx.Choice(self.panel, -1, pos=(width6, height6), choices=['3'], size=(120, -1))
        self.labels_choice.Disable()

        self.__static_text(pos=(width1, height7), label='Sprint')
        self.sprint_choice = wx.Choice(self.panel, -1, pos=(width2, height7), choices=['1'], size=(120, -1))
        self.sprint_choice.Disable()

        self.__static_text(pos=(width3, height7), label='Category Type')
        self.category_type_choice = wx.Choice(self.panel, -1, pos=(width4, height7), choices=ic.category_type.get(ic.choice), size=(120, -1))

        self.__static_text(pos=(width1, height8), label='Summary*')
        self.summary_input = wx.TextCtrl(self.panel, -1, pos=(width2, height8), size=(590, -1))

        self.__static_text(pos=(width1, height9), label='Description*')
        self.description_input = wx.TextCtrl(self.panel, -1, pos=(width2, height9), size=(590, 300), style=wx.TE_MULTILINE)


        self.__static_text(pos=(width1, height10), label='Log link*')
        self.log_link_input = wx.TextCtrl(self.panel, -1, pos=(width2, height10), size=(590, -1))

        self.__static_text(pos=(width1, height11), label='SR Number')
        self.sr_number_input = wx.TextCtrl(self.panel, -1, pos=(width2, height11), size=(240, -1))

        self.__static_text(pos=(width7, height11), label='External JIRA ID')
        self.external_jira_id_input = wx.TextCtrl(self.panel, -1, pos=(width8, height11), size=(240, -1))

        self.__static_text(pos=(width1, height12), label='Serial Number')
        self.serial_number_input = wx.TextCtrl(self.panel, -1, pos=(width2, height12), size=(240, -1))

        self.__static_text(pos=(width7, height12), label='MCN number')
        self.mcn_number_input = wx.TextCtrl(self.panel, -1, pos=(width8, height12), size=(240, -1))

        self.__static_text(pos=(width1, height13), label='MetaBuildLocation')
        self.meta_build_location_input = wx.TextCtrl(self.panel, -1, pos=(width2, height13), size=(590, -1))

        create_button = wx.Button(self.panel, -1, label='Create', pos=(550, height14), size=(80, 30))
        cancel_button = wx.Button(self.panel, wx.ID_CANCEL, label='Cancel', pos=(635, height14), size=(80, 30))
        import_button = wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=wx.Bitmap("C:\Users\c_youwu\PycharmProjects\AutoJIRA\\resource\icon\import.png", wx.BITMAP_TYPE_PNG), pos=(width1 + 18, height14 + 8), size=(34, 34))
        export_button = wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=wx.Bitmap("C:\Users\c_youwu\PycharmProjects\AutoJIRA\\resource\icon\export.png", wx.BITMAP_TYPE_PNG), pos=(width1 + 52, height14 + 8), size=(34, 34))
        save_button = wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=wx.Bitmap("C:\Users\c_youwu\PycharmProjects\AutoJIRA\\resource\icon\export.png", wx.BITMAP_TYPE_PNG), pos=(width1 + 86, height14 + 8), size=(34, 34))
        self.Bind(wx.EVT_BUTTON, self.on_create, create_button)

    def on_components(self, event):
        components = ComponentsDialog(self.component_input.GetValue(), self.Position)
        result = components.ShowModal()
        if result == wx.ID_OK:
            self.component_input.SetValue(components.get_checked_item())
        components.Destroy()

    def on_assignee(self, event):
        print 'Not Ready'

    def on_create(self, event):
        if not self.__check_required_item_is_correct():
            return
        dict_issue = Issue.generate(self)
        jira = JIRA('qrd_automation', '1234Abcd')
        #print jira.post(data=dict_issue)

    def __check_required_item_is_correct(self):
        error_list = list()
        if not self.project_choice.GetStringSelection():
            error_list.append('Project')
        if not self.issue_type_choice.GetStringSelection():
            error_list.append('Issue Type')
        if not self.crash_choice.GetStringSelection():
            error_list.append('Crash')
        if not self.repeatability_choice.GetStringSelection():
            error_list.append('Repeatability')
        if not self.severity_choice.GetStringSelection():
            error_list.append('Severity')
        if not self.component_input.GetValue():
            error_list.append('Components')
        if not self.product_name_choice.GetStringSelection():
            error_list.append('Product Name')
        if not self.test_group_choice.GetStringSelection():
            error_list.append('Test Group')
        if not self.test_phase_choice.GetStringSelection():
            error_list.append('Test Phase')
        if not self.summary_input.GetValue():
            error_list.append('Summary')
        if not self.description_input.GetValue():
            error_list.append('Description')
        if not self.log_link_input.GetValue():
            error_list.append('Log Link')
        if error_list:
            msg = wx.MessageDialog(self.panel, message='Please complete with the information required!\n\n' + '\n'.join(error_list),
                                   caption="Error", style=wx.OK, pos=wx.DefaultPosition)
            msg.ShowModal()
            msg.Destroy()
            return False
        return True

    def __change_options(self, profile):
        if exists(path=profile):
            profile = libs.Utility.parse_profile(profile_path=profile)
            self.__change_options_from_profile(profile)
        else:
            self.__change_options_from_class_default()

    def __change_options_from_class_default(self):
        self.project_choice.SetStringSelection(ic.project.get(ic.default))
        self.issue_type_choice.SetStringSelection(ic.issue_type.get(ic.default))
        self.crash_choice.SetStringSelection(ic.crash.get(ic.default))
        self.repeatability_choice.SetStringSelection(ic.repeatability.get(ic.default))
        self.severity_choice.SetStringSelection(ic.severity.get(ic.default))
        self.component_input.SetValue(ic.components.get(ic.default))
        self.product_name_choice.SetStringSelection(ic.product_name.get(ic.default))
        self.test_group_choice.SetStringSelection(ic.test_group.get(ic.default))
        self.test_phase_choice.SetStringSelection(ic.test_phase.get(ic.default))
        self.area_choice.SetStringSelection(ic.area.get(ic.default))
        self.la_functionality_choice.SetStringSelection(ic.la_functionality.get(ic.default))
        self.mm_functionality_choice.SetStringSelection(ic.mm_functionality.get(ic.default))
        self.ui_functionality_choice.SetStringSelection(ic.ui_functionality.get(ic.default))
        self.cnss_functionality_choice.SetStringSelection(ic.cnss_functionality.get(ic.default))
        self.bsp_functionality_choice.SetStringSelection(ic.bsp_functionality.get(ic.default))
        self.assignee_input.SetValue(ic.assignee.get(ic.default))
        self.customer_name_choice.SetStringSelection(ic.customer_name.get(ic.default))
        # labels
        # sprint
        self.category_type_choice.SetStringSelection(ic.category_type.get(ic.default))
        self.summary_input.SetValue(ic.summary.get(ic.default))
        self.description_input.SetValue(ic.description.get(ic.default))
        self.log_link_input.SetValue(ic.log_link.get(ic.default))
        self.sr_number_input.SetValue(ic.sr_number.get(ic.default))
        self.external_jira_id_input.SetValue(ic.external_jira_id.get(ic.default))
        self.serial_number_input.SetValue(ic.serial_number.get(ic.default))
        self.mcn_number_input.SetValue(ic.mcn_number.get(ic.default))
        self.meta_build_location_input.SetValue(ic.meta_build_location.get(ic.default))

    def __change_options_from_profile(self, profile):
        self.project_choice.SetStringSelection(profile.get(ic.project.get(ic.name)))
        self.issue_type_choice.SetStringSelection(profile.get(ic.issue_type.get(ic.name)))
        self.crash_choice.SetStringSelection(profile.get(ic.crash.get(ic.name)))
        self.repeatability_choice.SetStringSelection(profile.get(ic.repeatability.get(ic.name)))
        self.severity_choice.SetStringSelection(profile.get(ic.severity.get(ic.name)))
        self.component_input.SetValue(profile.get(ic.components.get(ic.name)))
        self.product_name_choice.SetStringSelection(profile.get(ic.product_name.get(ic.name)))
        self.test_group_choice.SetStringSelection(profile.get(ic.test_group.get(ic.name)))
        self.test_phase_choice.SetStringSelection(profile.get(ic.test_phase.get(ic.name)))
        self.area_choice.SetStringSelection(profile.get(ic.area.get(ic.name)))
        self.la_functionality_choice.SetStringSelection(profile.get(ic.la_functionality.get(ic.name)))
        self.mm_functionality_choice.SetStringSelection(profile.get(ic.mm_functionality.get(ic.name)))
        self.ui_functionality_choice.SetStringSelection(profile.get(ic.ui_functionality.get(ic.name)))
        self.cnss_functionality_choice.SetStringSelection(profile.get(ic.cnss_functionality.get(ic.name)))
        self.bsp_functionality_choice.SetStringSelection(profile.get(ic.bsp_functionality.get(ic.name)))
        self.assignee_input.SetValue(profile.get(ic.assignee.get(ic.name)))
        self.customer_name_choice.SetStringSelection(profile.get(ic.customer_name.get(ic.name)))
        # labels
        # sprint
        self.category_type_choice.SetStringSelection(profile.get(ic.category_type.get(ic.name)))
        self.summary_input.SetValue(profile.get(ic.summary.get(ic.name)))
        self.description_input.SetValue(profile.get(ic.description.get(ic.name)))
        self.log_link_input.SetValue(profile.get(ic.log_link.get(ic.name)))
        self.sr_number_input.SetValue(profile.get(ic.sr_number.get(ic.name)))
        self.external_jira_id_input.SetValue(profile.get(ic.external_jira_id.get(ic.name)))
        self.serial_number_input.SetValue(profile.get(ic.serial_number.get(ic.name)))
        self.mcn_number_input.SetValue(profile.get(ic.mcn_number.get(ic.name)))
        self.meta_build_location_input.SetValue(profile.get(ic.meta_build_location.get(ic.name)))

class ComponentsDialog(wx.Dialog):
    def __init__(self, items, pos):
        wx.Dialog.__init__(self, None, -1, title="Components", size=(210, 253))
        panel = wx.Panel(self)
        x, y = pos
        self.SetPosition((x+720, y+70))
        self.components = wx.CheckListBox(panel, -1, choices=ic.components.get(ic.choice), size=(207, 190))
        self.__set_check_item(items=items)
        wx.Button(panel, wx.ID_OK, label='Y', pos=(138, 190), size=(33,  33))
        wx.Button(panel, wx.ID_CANCEL, label='N', pos=(172, 190), size=(33, 33))

    def get_checked_item(self):
        checked_tuple = self.components.GetCheckedStrings()
        return '|'.join(checked_tuple)

    def __set_check_item(self, items):
        if not items:
            return
        items = items.strip('|')
        item_list = items.split('|')
        check_list = list()
        for x in xrange(self.components.Count):
            if self.components.GetString(x) in item_list:
                check_list.append(x)
        self.components.SetChecked(check_list)


class LabelDialog(wx.Dialog):
    def __init__(self, items, pos):
        wx.Dialog.__init__(self, None, -1, title="Label", size=(210, 253))
        panel = wx.Panel(self)
        x, y = pos
        self.SetPosition((x+720, y+70))
        self.components = wx.CheckListBox(panel, -1, choices=ic.components.get(ic.choice), size=(207, 190))
        self.__set_check_item(items=items)
        wx.Button(panel, wx.ID_OK, label='Y', pos=(138, 190), size=(33,  33))
        wx.Button(panel, wx.ID_CANCEL, label='N', pos=(172, 190), size=(33, 33))




if __name__ == '__main__':
    import time
    print time.time()
    app = wx.App()
    print time.time()
    login = IssueDialog()
    print time.time()
    login.Show()
    print time.time()
    app.MainLoop()
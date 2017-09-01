import IssueConfiguration as ic
from libs.GlobalVariable import account

def generate(issue_dialog):
    issue = dict()
    issue['fields'] = __fields(issue_dialog)
    return issue


def __fields(issue_dialog):
    fields = dict()
    fields[ic.project.get(ic.id)] = __project(issue_dialog)
    fields[ic.issue_type.get(ic.id)] = __issue_type(issue_dialog)
    fields[ic.crash.get(ic.id)] = __crash(issue_dialog)
    fields[ic.repeatability.get(ic.id)] = __repeatability(issue_dialog)
    fields[ic.severity.get(ic.id)] = __severity(issue_dialog)
    fields[ic.components.get(ic.id)] = __components(issue_dialog)
    fields[ic.product_name.get(ic.id)] = __product_name(issue_dialog)
    fields[ic.test_group.get(ic.id)] = __test_group(issue_dialog)
    fields[ic.test_phase.get(ic.id)] = __test_phase(issue_dialog)
    fields[ic.area.get(ic.id)] = __area(issue_dialog)
    fields[ic.la_functionality.get(ic.id)] = __la_functionality(issue_dialog)
    fields[ic.mm_functionality.get(ic.id)] = __mm_functionality(issue_dialog)
    fields[ic.ui_functionality.get(ic.id)] = __ui_functionality(issue_dialog)
    fields[ic.cnss_functionality.get(ic.id)] = __cnss_functionality(issue_dialog)
    fields[ic.bsp_functionality.get(ic.id)] = __bsp_functionality(issue_dialog)
    fields[ic.assignee.get(ic.id)] = __assignee(issue_dialog)
    fields[ic.customer_name.get(ic.id)] = __customer_name(issue_dialog)
    fields[ic.labels.get(ic.id)] = __labels(issue_dialog)
    #sprint
    fields[ic.category_type.get(ic.id)] = __category_type(issue_dialog)
    fields[ic.summary.get(ic.id)] = __summary(issue_dialog)
    fields[ic.description.get(ic.id)] = __description(issue_dialog)
    fields[ic.log_link.get(ic.id)] = __log_link(issue_dialog)
    fields[ic.sr_number.get(ic.id)] = __sr_number(issue_dialog)
    fields[ic.external_jira_id.get(ic.id)] = __external_jira_id(issue_dialog)
    fields[ic.serial_number.get(ic.id)] = __serial_number(issue_dialog)
    fields[ic.mcn_number.get(ic.id)] = __mcn_number(issue_dialog)
    fields[ic.meta_build_location.get(ic.id)] = __meta_build_location(issue_dialog)
    return fields


def __customer_name(issue_dialog):
    customer_name = dict()
    customer_name['value'] = issue_dialog.customer_name_choice.GetStringSelection()
    return customer_name


def __category_type(issue_dialog):
    category_type = dict()
    category_type['value'] = issue_dialog.category_type_choice.GetStringSelection()
    return category_type


def __sr_number(issue_dialog):
    return issue_dialog.sr_number_input.GetValue()[:255]


def __external_jira_id(issue_dialog):
    return issue_dialog.external_jira_id_input.GetValue()[:255]


def __serial_number(issue_dialog):
    return issue_dialog.serial_number_input.GetValue()[:255]


def __mcn_number(issue_dialog):
    return issue_dialog.mcn_number_input.GetValue()[:255]


def __meta_build_location(issue_dialog):
    return issue_dialog.meta_build_location_input.GetValue()[:255]


def __labels(issue_dialog):
    string = issue_dialog.labels_input.GetValue()
    labels = string.split('|')
    return labels


def __components(issue_dialog):
    string = issue_dialog.component_input.GetValue()
    components = string.split('|')
    component_list = list()
    for component in components:
        component_list.append({'name': component})
    return component_list

def __area(issue_dialog):
    area = dict()
    area['value'] = issue_dialog.area_choice.GetStringSelection()
    return area


def __cnss_functionality(issue_dialog):
    cnss_functionality = dict()
    cnss_functionality['value'] = issue_dialog.cnss_functionality_choice.GetStringSelection()
    return cnss_functionality


def __mm_functionality(issue_dialog):
    mm_functionality = dict()
    mm_functionality['value'] = issue_dialog.mm_functionality_choice.GetStringSelection()
    return mm_functionality


def __bsp_functionality(issue_dialog):
    bsp_functionality = dict()
    bsp_functionality['value'] = issue_dialog.bsp_functionality_choice.GetStringSelection()
    return bsp_functionality


def __ui_functionality(issue_dialog):
    ui_functionality = dict()
    ui_functionality['value'] = issue_dialog.ui_functionality_choice.GetStringSelection()
    return ui_functionality


def __la_functionality(issue_dialog):
    la_functionality = dict()
    la_functionality['value'] = issue_dialog.la_functionality_choice.GetStringSelection()
    return la_functionality


def __repeatability(issue_dialog):
    repeatability = dict()
    repeatability['value'] = issue_dialog.repeatability_choice.GetStringSelection()
    return repeatability


def __crash(issue_dialog):
    crash = dict()
    crash['value'] = issue_dialog.crash_choice.GetStringSelection()
    return crash


def __test_phase(issue_dialog):
    test_phase = dict()
    test_phase['value'] = issue_dialog.test_phase_choice.GetStringSelection()
    return test_phase

def __test_group(issue_dialog):
    test_group = dict()
    test_group['value'] = issue_dialog.test_group_choice.GetStringSelection()
    return test_group


def __project(issue_dialog):
    project =dict()
    project['key'] = issue_dialog.project_choice.GetStringSelection()
    return project

def __summary(issue_dialog):
    return issue_dialog.summary_input.GetValue()[:255]

def __description(issue_dialog):
    return issue_dialog.description_input.GetValue()[:32768]

def __issue_type(issue_dialog):
    issue_type = dict()
    issue_type['name'] = issue_dialog.issue_type_choice.GetStringSelection()
    return issue_type

def __severity(issue_dialog):
    severity = dict()
    severity['value'] = issue_dialog.severity_choice.GetStringSelection()
    return severity


def __product_name(issue_dialog):
    product_name = dict()
    product_name['value'] = issue_dialog.product_name_choice.GetStringSelection()
    return product_name


def __log_link(issue_dialog):
    return issue_dialog.log_link_input.GetValue()[:255]

def __assignee(issue_dialog):
    assignee_value = issue_dialog.assignee_input.GetValue()
    if assignee_value == 'Assign to me':
        assignee = dict()
        assignee['name'] = account
        assignee['emailAddress'] = '%s@qti.qualcomm.com' % account
        return assignee
    else:
        assignee = dict()
        assignee['name'] = assignee_value
        assignee['emailAddress'] = '%s@qti.qualcomm.com' % assignee_value
        return assignee





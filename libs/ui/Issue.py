import IssueConfiguration as ic


def generate(issue_dialog):
    issue = dict()
    issue['fields'] = __fields(issue_dialog)
    return issue

def __fields(issue_dialog):
    fields = dict()
    fields[ic.project.get(ic.id)] = __project(issue_dialog)
    fields[ic.summary.get(ic.id)] = __summary(issue_dialog)
    fields[ic.description.get(ic.id)] = __description(issue_dialog)
    fields[ic.issue_type.get(ic.id)] = __issue_type(issue_dialog)
    fields[ic.severity.get(ic.id)] = __severity(issue_dialog)
    fields[ic.log_link.get(ic.id)] = __log_link(issue_dialog)
    fields[ic.test_group.get(ic.id)] = __test_group(issue_dialog)
    fields[ic.test_phase.get(ic.id)] = __test_phase(issue_dialog)
    fields[ic.crash.get(ic.id)] = __crash(issue_dialog)
    fields[ic.repeatability.get(ic.id)] = __repeatability(issue_dialog)
    fields[ic.cnss_functionality.get(ic.id)] = __cnss_functionality(issue_dialog)
    fields[ic.mm_functionality.get(ic.id)] = __mm_functionality(issue_dialog)
    fields[ic.ui_functionality.get(ic.id)] = __ui_functionality(issue_dialog)
    fields[ic.bsp_functionality.get(ic.id)] = __bsp_functionality(issue_dialog)
    fields[ic.area.get(ic.id)] = __area(issue_dialog)
    fields[ic.assignee.get(ic.id)] = __assignee(issue_dialog)
    fields[ic.components.get(ic.id)] = __components(issue_dialog)
    return fields

def __components(issue_dialog):
    string = issue_dialog.component_input.GetValue()
    components = string.split('|')
    component_list= list()
    for component in components:
        component_list.append({'name': str(component)})
    return component_list

def __area(issue_dialog):
    area = dict()
    area['value'] = str(issue_dialog.area_choice.GetStringSelection())
    return area

def __cnss_functionality(issue_dialog):
    cnss_functionality = dict()
    cnss_functionality['value'] = str(issue_dialog.cnss_functionality_choice.GetStringSelection())
    return cnss_functionality

def __mm_functionality(issue_dialog):
    mm_functionality = dict()
    mm_functionality['value'] = str(issue_dialog.mm_functionality_choice.GetStringSelection())
    return mm_functionality

def __bsp_functionality(issue_dialog):
    bsp_functionality = dict()
    bsp_functionality['value'] = str(issue_dialog.bsp_functionality_choice.GetStringSelection())
    return bsp_functionality


def __ui_functionality(issue_dialog):
    ui_functionality = dict()
    ui_functionality['value'] = str(issue_dialog.ui_functionality_choice.GetStringSelection())
    return ui_functionality


def __repeatability(issue_dialog):
    repeatability = dict()
    repeatability['value'] = str(issue_dialog.repeatability_choice.GetStringSelection())
    return repeatability


def __crash(issue_dialog):
    crash = dict()
    crash['value'] = str(issue_dialog.crash_choice.GetStringSelection())
    return crash


def __test_phase(issue_dialog):
    test_phase = dict()
    test_phase['value'] = str(issue_dialog.test_phase_choice.GetStringSelection())
    return test_phase

def __test_group(issue_dialog):
    test_group = dict()
    test_group['value'] = str(issue_dialog.test_group_choice.GetStringSelection())
    return test_group


def __project(issue_dialog):
    project =dict()
    project['key'] = str(issue_dialog.project_choice.GetStringSelection())
    return project

def __summary(issue_dialog):
    return str(issue_dialog.summary_input.GetValue())

def __description(issue_dialog):
    return str(issue_dialog.description_input.GetValue())

def __issue_type(issue_dialog):
    issue_type = dict()
    issue_type['name'] = str(issue_dialog.issue_type_choice.GetStringSelection())
    return issue_type

def __severity(issue_dialog):
    severity = dict()
    severity['value'] = str(issue_dialog.severity_choice.GetStringSelection())
    return severity


def __product_name(issue_dialog):
    product_name = dict()
    product_name['value'] = str(issue_dialog.product_name_choice.GetStringSelection())
    return product_name


def __log_link(issue_dialog):
    return str(issue_dialog.log_link_input.GetValue())

def __product_name(issue_dialog):
    product_name = dict()
    product_name['value'] = str(issue_dialog.product_name_choice.GetStringSelection())
    return product_name

def __assignee(issue_dialog):
    assignee = dict()
    account = 'c_youwu'
    assignee['name'] = account
    assignee['emailAddress'] = '%s@qti.qualcomm.com' % account
    return assignee


data = {
        "components": [
            {
                "name": "AP-LA-Stability"
            }
        ],
        "customfield_14930": "10-NN519-110",
        "customfield_14929": "2a16f62"
    }


import yIssueConfiguration as ic
from libs import GlobalVariable


def generate(issue_dict):
    issue = dict()
    issue['fields'] = __fields(issue_dict)
    return issue


def __fields(issue_dict):
    fields = dict()
    fields[ic.project.get(ic.id)] = __project(issue_dict.get(ic.project.get(ic.name)))
    fields[ic.issue_type.get(ic.id)] = __issue_type(issue_dict.get(ic.issue_type.get(ic.name)))
    fields[ic.crash.get(ic.id)] = __crash(issue_dict.get(ic.crash.get(ic.name)))
    fields[ic.repeatability.get(ic.id)] = __repeatability(issue_dict.get(ic.repeatability.get(ic.name)))
    fields[ic.severity.get(ic.id)] = __severity(issue_dict.get(ic.severity.get(ic.name)))
    fields[ic.components.get(ic.id)] = __components(issue_dict.get(ic.components.get(ic.name)))
    fields[ic.product_name.get(ic.id)] = __product_name(issue_dict.get(ic.product_name.get(ic.name)))
    fields[ic.test_group.get(ic.id)] = __test_group(issue_dict.get(ic.test_group.get(ic.name)))
    fields[ic.test_phase.get(ic.id)] = __test_phase(issue_dict.get(ic.test_phase.get(ic.name)))
    fields[ic.area.get(ic.id)] = __area(issue_dict.get(ic.area.get(ic.name)))
    fields[ic.la_functionality.get(ic.id)] = __la_functionality(issue_dict.get(ic.la_functionality.get(ic.name)))
    fields[ic.mm_functionality.get(ic.id)] = __mm_functionality(issue_dict.get(ic.mm_functionality.get(ic.name)))
    fields[ic.ui_functionality.get(ic.id)] = __ui_functionality(issue_dict.get(ic.ui_functionality.get(ic.name)))
    fields[ic.cnss_functionality.get(ic.id)] = __cnss_functionality(issue_dict.get(ic.cnss_functionality.get(ic.name)))
    fields[ic.bsp_functionality.get(ic.id)] = __bsp_functionality(issue_dict.get(ic.bsp_functionality.get(ic.name)))
    fields[ic.assignee.get(ic.id)] = __assignee(issue_dict.get(ic.assignee.get(ic.name)))
    fields[ic.customer_name.get(ic.id)] = __customer_name(issue_dict.get(ic.customer_name.get(ic.name)))
    fields[ic.labels.get(ic.id)] = __labels(issue_dict.get(ic.labels.get(ic.name)))
    #sprint
    fields[ic.category_type.get(ic.id)] = __category_type(issue_dict.get(ic.category_type.get(ic.name)))
    fields[ic.summary.get(ic.id)] = __summary(issue_dict.get(ic.summary.get(ic.name)))
    fields[ic.description.get(ic.id)] = __description(issue_dict.get(ic.description.get(ic.name)))
    fields[ic.log_link.get(ic.id)] = __log_link(issue_dict.get(ic.log_link.get(ic.name)))
    fields[ic.sr_number.get(ic.id)] = __sr_number(issue_dict.get(ic.sr_number.get(ic.name)))
    fields[ic.external_jira_id.get(ic.id)] = __external_jira_id(issue_dict.get(ic.external_jira_id.get(ic.name)))
    fields[ic.serial_number.get(ic.id)] = __serial_number(issue_dict.get(ic.serial_number.get(ic.name)))
    fields[ic.mcn_number.get(ic.id)] = __mcn_number(issue_dict.get(ic.mcn_number.get(ic.name)))
    fields[ic.meta_build_location.get(ic.id)] = __meta_build_location(issue_dict.get(ic.meta_build_location.get(ic.name)))
    return fields


def __value_mapping_value(value):
    _dict = dict()
    if value:
        _dict['value'] = value
        return _dict
    else:
        return None


def __customer_name(value):
    return __value_mapping_value(value)


def __category_type(value):
    return __value_mapping_value(value)


def __sr_number(value):
    return value[:255]


def __external_jira_id(value):
    return value[:255]


def __serial_number(value):
    return value[:255]


def __mcn_number(value):
    return value[:255]


def __meta_build_location(value):
    return value[:255]


def __labels(value):
    labels = value.split('|')
    labels = list(set(labels))
    return labels


def __components(value):
    components = value.split('|')
    components = list(set(components))
    component_list = list()
    for component in components:
        component_list.append({'name': component})
    return component_list


def __area(value):
    return __value_mapping_value(value)


def __cnss_functionality(value):
    return __value_mapping_value(value)


def __mm_functionality(value):
    return __value_mapping_value(value)


def __bsp_functionality(value):
    return __value_mapping_value(value)


def __ui_functionality(value):
    return __value_mapping_value(value)


def __la_functionality(value):
    return __value_mapping_value(value)

def __repeatability(value):
    repeatability = dict()
    repeatability['value'] = value
    return repeatability


def __crash(value):
    crash = dict()
    crash['value'] = value
    return crash


def __test_phase(value):
    test_phase = dict()
    test_phase['value'] = value
    return test_phase

def __test_group(value):
    test_group = dict()
    test_group['value'] = value
    return test_group


def __project(value):
    project =dict()
    project['key'] = value
    return project

def __summary(value):
    return value[:255]

def __description(value):
    return value[:32768]

def __issue_type(value):
    issue_type = dict()
    issue_type['name'] = value
    return issue_type

def __severity(value):
    severity = dict()
    severity['value'] = value
    return severity


def __product_name(value):
    product_name = dict()
    product_name['value'] = value
    return product_name


def __log_link(value):
    return value[:255]


def __assignee(value):
    assignee_value = value
    if assignee_value == 'Assign to me':
        assignee = dict()
        assignee['name'] = GlobalVariable.account
        assignee['emailAddress'] = '%s@qti.qualcomm.com' % GlobalVariable.account
        return assignee
    else:
        assignee = dict()
        assignee['name'] = assignee_value
        assignee['emailAddress'] = '%s@qti.qualcomm.com' % assignee_value
        return assignee





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

    print fields



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
    return issue_dialog.summary_input.GetValue()

def __description(issue_dialog):
    return issue_dialog.description_input.GetValue()

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
    return issue_dialog.log_link_input.GetValue()

def __product_name(issue_dialog):
    product_name = dict()
    product_name['value'] = issue_dialog.product_name_choice.GetStringSelection()
    return product_name




data = {

        "customfield_12904": {
            "value": "No"
        },
        "customfield_10455": {
            "value": "Easily Replicates"
        },
        "customfield_23010": {
            "value": "NotWCNIssue"
        },
        "customfield_21725": {
            "value": "Linux_Stability_KernelStability"
        },
        "customfield_21726": {
            "value": "Not MM Issue"
        },
        "customfield_21727": {
            "value": "Not UI Issue"
        },
        "customfield_21736": {
            "value": "Not BSP Issue"
        },
        "customfield_10388": {
            "value": "LA"
        },
        "assignee": {
            "name": "c_youwu",
            "emailAddress": "c_youwu@qti.qualcomm.com"
        },
        # "creator":{
        #     "name": "c_youwu",
        #     "emailAddress": "c_youwu@qti.qualcomm.com"
        # },
        "components": [
            {
                "name": "AP-LA-Stability"
            }
        ],
        "customfield_14930": "10-NN519-110",
        "customfield_14929": "2a16f62"
    }
}

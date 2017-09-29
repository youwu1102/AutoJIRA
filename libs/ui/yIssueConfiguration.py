from libs import Utility
choice = 'choice'
default = 'default'
id = 'id'
name = 'name'

project = {
    name: 'Project',
    choice: ['CHNAPSS'],
    default: 'CHNAPSS',
    id: 'project'
}

issue_type = {
    name: 'Issue Type',
    choice: ['Bug'],
    default: 'Bug',
    id: 'issuetype'
}

crash = {
    name: 'Crash',
    choice: ['', 'No', 'Yes'],
    default: '',
    id: 'customfield_12904'
}

repeatability = {
    name: 'Repeatability',
    choice: ['', 'Not Attempted', 'Cannot Replicate', 'Replicates With Effort', 'Easily Replicates'],
    default: '',
    id: 'customfield_10455'
}

severity = {
    name: 'Severity',
    choice: ['', 'Blocker', 'Critical', 'Major', 'Moderate', 'Minor', 'Trivial', 'None Set', 'Cosmetic', 'HIGH', 'LOW', 'MEDIUM', 'UNKNOWN', 'None'],
    default: '',
    id: 'customfield_10102'
}

components ={
    name: 'Components',
    choice: ['AP-AU_Sanity', 'AP-3rdPartyAPK', 'AP-LA-Stability'],
    default: '',
    id: 'components'
}

product_name = {
    name: 'Product Name',
    choice: ['', 'SDM630.LA.2.0', 'APQ8009.LE.1.0.2', 'SDM660.LA.2.0', 'SDM845.LA.1.0', ''],
    default: '',
    id: 'customfield_21339'
}

test_group = {
    name: 'Test Group',
    choice: ['', 'AlphaCustomer', 'APT CHN', 'APT Pactera', 'APT QIPL', 'CE', 'CST CHN', 'CST CIENET', 'DTE',
             'MST CHN', 'PDT CHN', 'PDT CIENET NJ', 'PDT QIPL', 'APT NEU', 'CIT CHN', 'GP PAC', 'GP CHN',
             'FUT', 'PTT CHN'],
    default: '',
    id: 'customfield_11746'
}

test_phase = {
    name: 'Test Phase',
    choice: ['', 'Bring-Up', 'Pre-FC', 'Pre-Silicon', 'FC-to-CS', 'Post-CS'],
    default: '',
    id: 'customfield_10456'
}

area = {
    name: 'Area',
    choice: ['', 'BSP', 'BT', 'FM', 'GPS', 'LA', 'MM', 'NFC', 'UI', 'WLAN'],
    default: '',
    id: 'customfield_10388'
}

la_functionality = {
    name: 'LA Functionality',
    choice: Utility.parse_config('LA Functionality.xml'),
    default: '',
    id: 'customfield_21725'
}

mm_functionality = {
    name: 'MM Functionality',
    choice: Utility.parse_config('MM Functionality.xml'),
    default: '',
    id: 'customfield_21726'
}

ui_functionality = {
    name: 'UI Functionality',
    choice: Utility.parse_config('UI Functionality.xml'),
    default: '',
    id: 'customfield_21727'
}

cnss_functionality = {
    name: 'CNSS Functionality',
    choice: Utility.parse_config('CNSS Functionality.xml'),
    default: '',
    id: 'customfield_23010'
}

bsp_functionality = {
    name: 'BSP Functionality',
    choice: Utility.parse_config('BSP Functionality.xml'),
    default: '',
    id: 'customfield_21736'
}


assignee = {
    name: 'Assignee',
    choice: [],
    default: 'Assign to me',
    id: 'assignee'
}

customer_name = {
    name: 'Customer Name',
    choice: ['', 'BBK/Vivo', 'Datang', 'Feixun', 'Foxda', 'Gionee', 'Heyuan/Tinno', 'Hisense', 'Huaqin',
             'Huawei', 'Huiye', 'Internal', 'Lenovo', 'Longcheer', 'MOTO(Motorola)', 'OPPO', 'Others', 'TCL',
             'Tianyu/K-Touch', 'Wingtech', 'Xiaomi', 'Yulong/Coolpad', 'ZTE'],
    default: '',
    id: 'customfield_10805'
}

category_type = {
    name: 'Category Type',
    choice: ['', 'Function', 'Stability', 'Power', 'Performance', 'Compatibility', 'Thermal'],
    default: '',
    id: 'customfield_11073'
}

summary = {
    name: 'Summary',
    default: '',
    id: 'summary'
}

description = {
    name: 'Description',
    default: '',
    id: 'description'
}

log_link = {
    name: 'Log link',
    default: '',
    id: 'customfield_21324'
}

sr_number = {
    name: 'SR Number',
    default: '',
    id: 'customfield_12727'
}

external_jira_id = {
    name: 'External JIRA ID',
    default: '',
    id: 'customfield_21720'
}

serial_number = {
    name: 'Serial Number',
    default: '',
    id: 'customfield_14929'
}

mcn_number = {
    name: 'MCN number',
    default: '',
    id: 'customfield_14930'
}

meta_build_location = {
    name: 'Meta Build Location',
    default: '',
    id: 'customfield_14016'
}

labels = {
    name: 'Labels',
    choice: ['FrameworkReboot', 'UIFreeze', 'ANR', 'Tombstone', 'AppCrash', 'TZCrash', 'ModemCrash',
             'RPMCrash', 'WLANCrash'],
    default: '',
    id: 'labels'
}
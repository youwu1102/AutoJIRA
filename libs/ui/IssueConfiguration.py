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
    default: 'No',
    id: 'customfield_12904'
}

repeatability = {
    name: 'Repeatability',
    choice: ['', 'Not Attempted', 'Cannot Replicate', 'Replicates With Effort', 'Easily Replicates'],
    default: 'Easily Replicates',
    id: 'customfield_10455'
}

severity = {
    name: 'Severity',
    choice: ['', 'Blocker', 'Critical', 'Major', 'Moderate', 'Minor', 'Trivial', 'None Set', 'Cosmetic', 'HIGH', 'LOW', 'MEDIUM', 'UNKNOWN', 'None'],
    default: 'HIGH',
    id: 'customfield_10102'
}

components ={
    name: 'Components',
    choice: ['AP-AU_Sanity', 'AP-3rdPartyAPK', 'AP-LA-Stability', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9'],
    default: 'AP-LA-Stability',
    id: 'components'
}

product_name = {
    name: 'Product Name',
    choice: ['', '8909.3.0.1', '8940.2.0', '8996.2.0.2', '[APQ8084.LA.1.2.2.2 + MDM9635M.TN.2.0]',
             'android_ui_internal_dev_1.0', 'APQ8009.LE', 'APQ8009.LE.1.1', 'APQ8074.LE.1.1', 'APQ8074.LE.1.2',
             'APQ8096.LE.1.0', 'APSS.LA.0.0_FR', 'MSM8610.LA.1.0', 'MSM8610.LA.1.1', 'MSM8610.LA.1.8.3',
             'MSM8610.LA.1.8.7', 'MSM8610.LA.1.9', 'MSM8610.LA.1.9.1', 'MSM8610.LA.1.9.2', 'MSM8610.LA.1.9.3',
             'MSM8610.LA.2.0', 'MSM8610.LA.2.1', 'MSM8626.LA.1.04', 'MSM8905.LA.1.4', 'MSM8905.LF.1.2', 'MSM8909.LA.1.0',
             'MSM8909.LA.1.1', 'MSM8909.LA.1.1.c4', 'MSM8909.LA.1.2'],
    default: 'MSM8909.LA.1.1',
    id: 'customfield_21339'
}

test_group = {
    name: 'Test Group',
    choice: ['', 'AlphaCustomer', 'APT CHN', 'APT Pactera', 'APT QIPL', 'CE', 'CST CHN', 'CST CIENET', 'DTE',
             'MST CHN', 'PDT CHN', 'PDT CIENET NJ', 'PDT QIPL', 'APT NEU', 'CIT CHN', 'GP PAC', 'GP CHN',
             'FUT', 'PTT CHN'],
    default: 'APT CHN',
    id: 'customfield_11746'
}

test_phase = {
    name: 'Test Phase',
    choice: ['', 'Bring-Up', 'Pre-FC', 'Pre-Silicon', 'FC-to-CS', 'Post-CS'],
    default: 'Pre-FC',
    id: 'customfield_10456'
}

area = {
    name: 'Area',
    choice: ['', 'BSP', 'BT', 'FM', 'GPS', 'LA', 'MM', 'NFC', 'UI', 'WLAN'],
    default: 'LA',
    id: 'customfield_10388'
}

la_functionality = {
    name: 'LA Functionality',
    choice: ['', 'Not LA Issue', 'Android_Performance_Benchmarks', 'Android_Performance_Display', 'Android_Performance_Memory',
             'Android_Performance_MM', 'Android_Performance_Systems', 'Android_Telephony_Common', 'Android_Telephony_Data',
             'Android_Telephony_IMS', 'Android_Telephony_RIL', 'Android_Telephony_SMS/MMS', 'Android_Telephony_UIM/Contact/STK',
             'Android_Telephony_Voice', 'Boot', 'Charging', 'Clock', 'CTASecurity', 'CTS', 'Factory', 'FileSystem',
             'Linux_Stability_FrameworkStability', 'Linux_Stability_KernelStability', 'Linux_Stability_S2KernelStability',
             'Linux_Stability_S3SystemStability', 'LinuxCommon', 'Logging', 'Memory', 'OTA/Recovery', 'PMIC', 'Power',
             'QDSS', 'Sensors', 'ThermalDriver', 'Tools', 'Android_Telephony_IMS_VT', 'VRService', 'VRSDK', 'Drones_afc',
             'Drones_dspal', 'Drones_flight'],
    default: 'Linux_Stability_KernelStability',
    id: 'customfield_21725'
}

mm_functionality = {
    name: 'MM Functionality',
    choice: ['', 'Android_Audio_ACDB', 'Android_Audio_Codec_Driver', 'Android_Audio_Framework', 'Not MM Issue'],
    default: 'Not MM Issue',
    id: 'customfield_21726'
}

ui_functionality = {
    name: 'UI Functionality',
    choice: ['APP_Framework', 'Camera', 'China_Carrier_APPs', 'Contacts', 'Not UI Issue'],
    default: 'Not UI Issue',
    id: 'customfield_21727'
}

cnss_functionality = {
    name: 'CNSS Functionality',
    choice: ['', 'NotWCNIssue', 'WLAN_Host', 'WLAN_FW', 'WLAN_Coex', 'BT_Host', 'BT_FW', 'BT_Coex', 'FM_Host',
             'FM_FW', 'FM_Coex', 'NFC_Host', 'NFC_FW', 'NFC_Coex', 'GPS', 'Drones_connectivity'],
    default: 'NotWCNIssue',
    id: 'customfield_23010'
}

bsp_functionality = {
    name: 'BSP Functionality',
    choice: ['', 'BAM/TSENS/ADC', 'Clock', 'DDR', 'Diag/QMI/IPCRouter', 'Not BSP Issue'],
    default: 'Not BSP Issue',
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
    default: 'BBK/Vivo',
    id: 'customfield_10805'
}

category_type = {
    name: 'Category Type',
    choice: ['', 'Function', 'Stability', 'Power', 'Performance', 'Compatibility', 'Thermal'],
    default: 'Function',
    id: 'customfield_11073'
}

summary = {
    name: 'Summary',
    default: 'summary&summary[summary]',
    id: 'summary'
}

description = {
    name: 'Description',
    default: 'description\ndescription\ndescription\ndescription',
    id: 'description'
}

log_link = {
    name: 'Log link',
    default: '\\\\log_link',
    id: 'customfield_21324'
}

sr_number = {
    name: 'SR Number',
    default: 'sr_number',
    id: ''
}

external_jira_id = {
    name: 'External JIRA ID',
    default: 'external_jira_id',
    id: ''
}

serial_number = {
    name: 'Serial Number',
    default: 'serial_number',
    id: ''
}

mcn_number = {
    name: 'MCN number',
    default: 'mcn_number',
    id: ''
}

meta_build_location = {
    name: 'Meta Build Location',
    default: 'meta_build_location',
    id: ''
}
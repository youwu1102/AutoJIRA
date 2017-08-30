choice = 'choice'
default = 'default'
id = 'id'

project = {
    choice: ['CHNAPSS'],
    default: 'CHNAPSS',
    id: 'project'
}

issue_type = {
    choice: ['Bug'],
    default: 'Bug',
    id: 'issuetype'
}

crash = {
    choice: ['', 'No', 'YES'],
    default: 'No',
    id: 'customfield_12904'
}

repeatability = {
    choice: ['', 'Not Attempted', 'Cannot Replicate', 'Replicates With Effort', 'Easily Replicates'],
    default: 'Replicates With Effort'
}

severity = {
    choice: ['', 'Blocker', 'Critical', 'Major', 'Moderate', 'Minor', 'Trivial', 'None Set', 'Cosmetic', 'HIGH', 'LOW', 'MEDIUM', 'UNKNOWN', 'None'],
    default: 'HIGH',
    id: 'customfield_10102'
}

components ={
    choice: ['AP-AU_Sanity', 'AP-3rdPartyAPK', 'AP-LA-Stability', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9'],
    default: 'AP-LA-Stability'
}

product_name = {
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
    choice: ['', 'AlphaCustomer', 'APT CHN', 'APT Pactera', 'APT QIPL', 'CE', 'CST CHN', 'CST CIENET', 'DTE',
             'MST CHN', 'PDT CHN', 'PDT CIENET NJ', 'PDT QIPL', 'APT NEU', 'CIT CHN', 'GP PAC', 'GP CHN',
             'FUT', 'PTT CHN'],
    default: 'APT CHN',
    id: 'customfield_11746'
}

test_phase = {
    choice: ['', 'Bring-Up', 'Pre-FC', 'Pre-Silicon', 'FC-to-CS', 'Post-CS'],
    default: 'FC-to-CS',
    id: 'customfield_10456'
}

area = {
    choice: ['', 'BSP', 'BT', 'FM', 'GPS', 'LA', 'MM', 'NFC', 'UI', 'WLAN'],
    default: 'LA'
}

la_functionality = {
    choice: ['', 'Not LA Issue', 'Android_Performance_Benchmarks', 'Android_Performance_Display', 'Android_Performance_Memory',
             'Android_Performance_MM', 'Android_Performance_Systems', 'Android_Telephony_Common', 'Android_Telephony_Data',
             'Android_Telephony_IMS', 'Android_Telephony_RIL', 'Android_Telephony_SMS/MMS', 'Android_Telephony_UIM/Contact/STK',
             'Android_Telephony_Voice', 'Boot', 'Charging', 'Clock', 'CTASecurity', 'CTS', 'Factory', 'FileSystem',
             'Linux_Stability_FrameworkStability', 'Linux_Stability_KernelStability', 'Linux_Stability_S2KernelStability',
             'Linux_Stability_S3SystemStability', 'LinuxCommon', 'Logging', 'Memory', 'OTA/Recovery', 'PMIC', 'Power',
             'QDSS', 'Sensors', 'ThermalDriver', 'Tools', 'Android_Telephony_IMS_VT', 'VRService', 'VRSDK', 'Drones_afc',
             'Drones_dspal', 'Drones_flight'],
    default: 'Not LA Issue'
}

mm_functionality = {
    choice: ['', 'Android_Audio_ACDB', 'Android_Audio_Codec_Driver', 'Android_Audio_Framework', 'Not MM Issue'],
    default: 'Not MM Issue'
}

ui_functionality = {
    choice: ['APP_Framework', 'Camera', 'China_Carrier_APPs', 'Contacts', 'Not UI Issue'],
    default: 'Not UI Issue'
}

cnss_functionality = {
    choice: ['', 'NotWCNIssue', 'WLAN_Host', 'WLAN_FW', 'WLAN_Coex', 'BT_Host', 'BT_FW', 'BT_Coex', 'FM_Host',
             'FM_FW', 'FM_Coex', 'NFC_Host', 'NFC_FW', 'NFC_Coex', 'GPS', 'Drones_connectivity'],
    default: 'NotWCNIssue'
}

bsp_functionality = {
    choice: ['', 'BAM/TSENS/ADC', 'Clock', 'DDR', 'Diag/QMI/IPCRouter'],
    default: ''
}


assignee = {
    choice: [],
    default: 'Assign to me'
}

customer_name = {
    choice: ['', 'BBK/Vivo', 'Datang', 'Feixun', 'Foxda', 'Gionee', 'Heyuan/Tinno', 'Hisense', 'Huaqin',
             'Huawei', 'Huiye', 'Internal', 'Lenovo', 'Longcheer', 'MOTO(Motorola)', 'OPPO', 'Others', 'TCL',
             'Tianyu/K-Touch', 'Wingtech', 'Xiaomi', 'Yulong/Coolpad', 'ZTE'],
    default: ''
}

category_type = {
    choice: ['', 'Function', 'Stability', 'Power', 'Performance', 'Compatibility', 'Thermal'],
    default: ''
}

summary = {
    default: 'JIRA summary',
    id: 'summary'
}

description = {
    default: 'Just a test for JIRA API',
    id: 'description'
}

log_link = {
    default: '\\APTCN'
}
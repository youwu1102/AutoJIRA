import urllib2
import urllib
from base64 import encodestring
import json
import cookielib
import GlobalVariable
import traceback
import time
        # self.data={
        #     "fields": {
        #         "project": {
        #           "key": "CHNAPSS"
        #         },
        #         "summary": "JIRA summary",
        #         "description": "Just a test for JIRA API",
        #         "issuetype": {
        #           "name": "Bug"
        #         },
        #         "customfield_10102": {
        #           "value": "Critical"
        #         },
        #         "customfield_21339": {
        #           "value": "MSM8939.LA.1.1"
        #         },
        #         "customfield_21324": "\\\\dine\\CHPDT",
        #         "customfield_11746": {
        #           "value": "PDT CHN"
        #         },
        #         "customfield_10456": {
        #           "value": "Pre-FC"
        #         },
        #         "customfield_12904": {
        #           "value": "No"
        #         },
        #         "customfield_10455": {
        #           "value": "Easily Replicates"
        #         },
        #         "customfield_23010": {
        #           "value": "NotWCNIssue"
        #         },
        #         "customfield_21725": {
        #           "value": "Linux_Stability_KernelStability"
        #         },
        #         "customfield_21726": {
        #           "value": "Not MM Issue"
        #         },
        #         "customfield_21727": {
        #           "value": "Not UI Issue"
        #         },
        #         "customfield_21736": {
        #           "value": "Not BSP Issue"
        #         },
        #         "customfield_10388": {
        #           "value": "LA"
        #         },
        #         "assignee": {
        #           "name": "c_youwu",
        #           "emailAddress": "c_youwu@qti.qualcomm.com"
        #         },
        #         # "creator":{
        #         #     "name": "c_youwu",
        #         #     "emailAddress": "c_youwu@qti.qualcomm.com"
        #         # },
        #         "components": [
        #           {
        #             "name": "AP-LA-Stability"
        #           }
        #         ],
        #         "customfield_14930": "10-NN519-110",
        #         "customfield_14929": "2a16f62"
        #     }
        # }

def aaa():

    url = 'https://udm-hss-jira.rnd.ki.sw.ericsson.se/jira/rest/api/2/search?jql='
    search = 'status%20%3D%20"In%20Progress"%20AND%20assignee%20in%20(currentUser())'
    # a = urllib.quote('search')
    # b = search.replace(' ', '%20')
    #req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/rest/api/2/search?jql=project+in+(CHNAPSS)+and+status+in+(Closed)+&maxResults=1&startAt=0')
    req = urllib2.Request(url + search)
    print req.get_full_url()
    req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (GlobalVariable.account, GlobalVariable.password))[:-1])
    response = urllib2.urlopen(req)
    print response.read()


def qurey(search, start):
    basic_url = 'https://udm-hss-jira.rnd.ki.sw.ericsson.se/jira/rest/api/2/search/?jql='
    url = basic_url + search + '&maxResults=100&startAt=%s' % start
    return __get(url=url, account=GlobalVariable.account, password=GlobalVariable.password)


def __get(url, account, password):
    # cookie = cookielib.LWPCookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # urllib2.install_opener(opener)
    headers = {'Authorization': 'Basic %s' % encodestring('%s:%s' % (account, password))[:-1]}
    request = urllib2.Request(url=url,headers=headers)
    try:
        response = urllib2.urlopen(request).read()
        return 0, response, ''
    except urllib2.HTTPError:
        return 1, '', traceback.format_exc()
    except urllib2.URLError:
        return 2, '', traceback.format_exc()

def create(data, account, password):
    # time.sleep(1)
    # return 0, str({"id": "7044855", "key": "CHNAPSS-51750",
    #            "self": "https://jira-cstm-tools.qualcomm.com/jira/rest/api/2/issue/7044855"}), ''
    return __post(data=data, account=account, password=password)


def __post(data, account, password):
    # cookie = cookielib.LWPCookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # urllib2.install_opener(opener)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % encodestring('%s:%s' % (account, password))[:-1],
        'Accept': '*/*'
    }
    request = urllib2.Request(url='https://jira-cstm-tools.qualcomm.com/jira/rest/api/2/issue',
                              headers=headers, data=json.dumps(data))
    try:
        response = urllib2.urlopen(request).read()
        return 0, response, ''
    except urllib2.HTTPError:
        return 1, '', traceback.format_exc()
    except urllib2.URLError:
        return 2, '', traceback.format_exc()


def authorization(account, password):
    cookie = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    req = urllib2.Request('https://udm-hss-jira.rnd.ki.sw.ericsson.se/login.jsp')
    req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (account, password))[:-1])
    try:
        urllib2.urlopen(req)
        return 0, 'Success', ''
    except urllib2.HTTPError:
        return 1, 'Authorization Fail', traceback.format_exc()
    except urllib2.URLError:
        return 2, 'Connection Fail', traceback.format_exc()


if __name__ == '__main__':
    import time
    import Utility
    print time.time()
    authorization(GlobalVariable.account, GlobalVariable.password)
    print time.time()
    aaa()
    # dict1 = {"issueTable":{"columnSortJql":{"reporter":"status = \"In Progress\" ORDER BY reporter ASC","summary":"status = \"In Progress\" ORDER BY summary ASC","customfield_10805":"status = \"In Progress\" ORDER BY cf[10805] ASC","issuekey":"status = \"In Progress\" ORDER BY key ASC","issuetype":"status = \"In Progress\" ORDER BY issuetype DESC","updated":"status = \"In Progress\" ORDER BY updated DESC","created":"status = \"In Progress\" ORDER BY created DESC","status":"status = \"In Progress\" ORDER BY status DESC","priority":"status = \"In Progress\" ORDER BY priority DESC","labels":"status = \"In Progress\" ORDER BY labels ASC","duedate":"status = \"In Progress\" ORDER BY due DESC","assignee":"status = \"In Progress\" ORDER BY assignee ASC","resolution":"status = \"In Progress\" ORDER BY resolution ASC","customfield_10803":"status = \"In Progress\" ORDER BY cf[10803] ASC"},"description":"","displayed":50,"end":50,"issueIds":[32586,32502,32443,32173,32014,31701,28628,22916,22469,19000,32749,32746,32745,32658,32580,32505,32479,32476,32291,32290,32113,31993,31992,31989,31987,31983,31982,19681,27328,23170,19173,18729,31042,30887,30540,29640,29340,27786,27602,25595,24856,24807,24052,23790,23509,23363,23282,31626,31221,30623,30255,29826,29430,29429,28361,28303,32771,32763,32753,32688,32675,32618,32590,32567,32491,32374,32125,32082,31914,31640,31503,31342,30588,30579,30687,29099,32761,32739,32701,32654,32649,32575,32346,32229,30852,32778,32759,32735,32711,32475,32462,32425,32409,32386,32263,32235,32165,32026,31839,31788,31659,31639,31575,31307,30030,29327,27429,32656,32650,29605,29417,28663,32516,32420,32397,32241,32174,32168,31897,31736,31445,31393,30573,29516,29229,28617,28149,32772,32521,32217,32124,31969,31899,31176,31158,30901,12931,12930,12916,12914,12907,12905,12904,12900,12898,12888,12884,12882,12877,12875,12874,12873,12872,32640,30720,31918,28402,26921,31870,31685,31683,31680,31679,31677,19149,18183],"issueKeys":["PLM-1261","PLM-1259","PLM-1253","PLM-1241","PLM-1229","PLM-1212","HSSTR-413","HSSTR-336","HSSTR-328","HSSLV-3","HSSJCAT-70","HSSJCAT-69","HSSJCAT-68","HSSJCAT-62","HSSJCAT-57","HSSJCAT-53","HSSJCAT-51","HSSJCAT-50","HSSJCAT-43","HSSJCAT-42","HSSJCAT-33","HSSJCAT-19","HSSJCAT-18","HSSJCAT-15","HSSJCAT-13","HSSJCAT-9","HSSJCAT-8","HSSIMPROVE-117","HSSFTIMP-25","HSSFTIMP-14","HSSFTIMP-6","HSSFTIMP-3","HSSFTC-218","HSSFTC-216","HSSFTC-211","HSSFTC-200","HSSFTC-196","HSSFTC-166","HSSFTC-165","HSSFTC-116","HSSFTC-76","HSSFTC-69","HSSFTC-41","HSSFTC-29","HSSFTC-22","HSSFTC-17","HSSFTC-11","HSSESTINT-85","HSSESTINT-84","HSSESTINT-76","HSSESTINT-69","HSSESTINT-58","HSSESTINT-52","HSSESTINT-51","HSSESTINT-6","HSSESTINT-2","HSSEST-4055","HSSEST-4053","HSSEST-4050","HSSEST-4031","HSSEST-4027","HSSEST-4019","HSSEST-4013","HSSEST-4007","HSSEST-3992","HSSEST-3964","HSSEST-3915","HSSEST-3908","HSSEST-3879","HSSEST-3806","HSSEST-3752","HSSEST-3717","HSSEST-3493","HSSEST-3491","HSSECM-71","HSSECM-62","HSSDM-2598","HSSDM-2594","HSSDM-2589","HSSDM-2586","HSSDM-2584","HSSDM-2582","HSSDM-2571","HSSDM-2561","HSSDM-2491","HSSDFU-1682","HSSDFU-1681","HSSDFU-1680","HSSDFU-1679","HSSDFU-1674","HSSDFU-1672","HSSDFU-1665","HSSDFU-1663","HSSDFU-1662","HSSDFU-1654","HSSDFU-1653","HSSDFU-1650","HSSDFU-1646","HSSDFU-1630","HSSDFU-1623","HSSDFU-1618","HSSDFU-1617","HSSDFU-1614","HSSDFU-1604","HSSDFU-1537","HSSDFU-1477","HSSDFU-1316","HSSCMTEAM-2427","HSSCMTEAM-2425","HSSCMTEAM-2088","HSSCMTEAM-2068","HSSCMTEAM-1948","HSSCIINT-187","HSSCIINT-185","HSSCIINT-184","HSSCIINT-183","HSSCIINT-181","HSSCIINT-180","HSSCIINT-177","HSSCIINT-171","HSSCIINT-160","HSSCIINT-150","HSSCIINT-129","HSSCIINT-104","HSSCIINT-92","HSSCIINT-45","HSSCIINT-5","HSSCI-2031","HSSCI-2002","HSSCI-1957","HSSCI-1939","HSSCI-1913","HSSCI-1901","HSSCI-1813","HSSCI-1810","HSSCI-1759","HQI-77","HQI-76","HQI-62","HQI-60","HQI-53","HQI-51","HQI-50","HQI-46","HQI-44","HQI-34","HQI-30","HQI-28","HQI-23","HQI-21","HQI-20","HQI-19","HQI-18","HPW-189","HPW-33","HCS-254","HCS-203","HCS-132","HCORE-32","HCORE-19","HCORE-17","HCORE-14","HCORE-13","HCORE-11","CIIOPER-20","CIIOPER-8"],"jiraHasIssues":true,"page":0,"pageSize":50,"startIndex":0,"table":[{"id":32586,"key":"PLM-1261","status":"In Progress","summary":"High Failure rate of IDR to MME","type":{"description":"Support task requested by PLM or other external source.","name":"Ticket","iconUrl":"/images/icons/issuetypes/exclamation.png"}},{"id":32502,"key":"PLM-1259","status":"In Progress","summary":"upgrade from HSS-FE 16A FD1 CP2 (CXP 903 3791/1 R3A17) to HSS-FE FD1 CP8","type":{"description":"Support task requested by PLM or other external source.","name":"Ticket","iconUrl":"/images/icons/issuetypes/exclamation.png"}},{"id":32443,"key":"PLM-1253","status":"In Progress","summary":"Confirmation about net.ipv4.conf.all.rp_filter needed from PDU","type":{"description":"Support task requested by PLM or other external source.","name":"Ticket","iconUrl":"/images/icons/issuetypes/exclamation.png"}},{"id":32173,"key":"PLM-1241","status":"In Progress","summary":"HSSFE 1 do not send IDR after PUR ( STN-SR update ) is received","type":{"description":"Support task requested by PLM or other external source.","name":"Ticket","iconUrl":"/images/icons/issuetypes/exclamation.png"}},{"id":32014,"key":"PLM-1229","status":"In Progress","summary":"Analysis of core dumps (TTX15330/CSR3270120)","type":{"description":"Support task requested by PLM or other external source.","name":"Ticket","iconUrl":"/images/icons/issuetypes/exclamation.png"}},{"id":31701,"key":"PLM-1212","status":"In Progress","summary":"PG to HSS_IMS notification failed ","type":{"description":"Support task requested by PLM or other external source.","name":"Ticket","iconUrl":"/images/icons/issuetypes/exclamation.png"}},{"id":28628,"key":"HSSTR-413","status":"In Progress","summary":"Distribution of traffic throught mmes is not balanced, impacting EPC traffic in big environments","type":{"description":"Ticket used to report BAT issues","name":"ST Ticket","iconUrl":"/secure/viewavatar?size=xsmall&avatarId=11000&avatarType=issuetype"}},{"id":22916,"key":"HSSTR-336","status":"In Progress","summary":"Short range of subsribers in BAT to use big environments (TSP)","type":{"description":"Ticket used to report BAT issues","name":"ST Ticket","iconUrl":"/secure/viewavatar?size=xsmall&avatarId=11000&avatarType=issuetype"}},{"id":22469,"key":"HSSTR-328","status":"In Progress","summary":"Clarify the correct flow for ISM-340 in the BAT Spec PA10","type":{"description":"Ticket used to report BAT issues","name":"ST Ticket","iconUrl":"/secure/viewavatar?size=xsmall&avatarId=11000&avatarType=issuetype"}},{"id":19000,"key":"HSSLV-3","status":"In Progress","summary":"installation of LSV4","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32749,"key":"HSSJCAT-70","status":"In Progress","summary":"CBA dummy upgrade failed but report success","type":{"description":"A problem which impairs or prevents the functions of the product.","name":"Bug","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":32746,"key":"HSSJCAT-69","status":"In Progress","summary":"Add Extra Parameter For Test Cps Case","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32745,"key":"HSSJCAT-68","status":"In Progress","summary":"Add Test Validation For Test Cps Case","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32658,"key":"HSSJCAT-62","status":"In Progress","summary":"CPS Calculation refactor","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":32580,"key":"HSSJCAT-57","status":"In Progress","summary":"Use log4j2","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32505,"key":"HSSJCAT-53","status":"In Progress","summary":"Run case with new fw R4C29-alpha-1","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32479,"key":"HSSJCAT-51","status":"In Progress","summary":"collectVDicosStats parase error","type":{"description":"A problem which impairs or prevents the functions of the product.","name":"Bug","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":32476,"key":"HSSJCAT-50","status":"In Progress","summary":"[JCAT FW] Run case with new fw","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32291,"key":"HSSJCAT-43","status":"In Progress","summary":"[CBA] TC-STAB-0421: Long Stability - HLR","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32290,"key":"HSSJCAT-42","status":"In Progress","summary":"[CBA] TC-STAB-0420 : Long Stability - AVG","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":32113,"key":"HSSJCAT-33","status":"In Progress","summary":"[CBA] TC-CROB-0500","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":31993,"key":"HSSJCAT-19","status":"In Progress","summary":"[JCAT FW] Use latest JCAT FW R4","type":{"description":"Created by JIRA Agile - do not edit or delete. Issue type for a user story.","name":"Story","iconUrl":"/images/icons/issuetypes/story.png"}},{"id":31992,"key":"HSSJCAT-18","status":"In Progress","summary":"[JCAT_ROBOT] Rosetta DataBase interface for new cabinet's ip address","type":{"description":"Created by JIRA Agile - do not edit or delete. Issue type for a user story.","name":"Story","iconUrl":"/images/icons/issuetypes/story.png"}},{"id":31989,"key":"HSSJCAT-15","status":"In Progress","summary":"[TSP] TSP CL2 adaption","type":{"description":"Created by JIRA Agile - do not edit or delete. Issue type for a user story.","name":"Story","iconUrl":"/images/icons/issuetypes/story.png"}},{"id":31987,"key":"HSSJCAT-13","status":"In Progress","summary":"[JCAT FW] Analysing the architecture of HSS JCAT ","type":{"description":"Created by JIRA Agile - do not edit or delete. Issue type for a user story.","name":"Story","iconUrl":"/images/icons/issuetypes/story.png"}},{"id":31983,"key":"HSSJCAT-9","status":"In Progress","summary":"[CBA] CUDB support","type":{"description":"Created by JIRA Agile - do not edit or delete. Issue type for a user story.","name":"Story","iconUrl":"/images/icons/issuetypes/story.png"}},{"id":31982,"key":"HSSJCAT-8","status":"In Progress","summary":"[TSP] HW Pooling SAUROM","type":{"description":"Created by JIRA Agile - do not edit or delete. Issue type for a user story.","name":"Story","iconUrl":"/images/icons/issuetypes/story.png"}},{"id":19681,"key":"HSSIMPROVE-117","status":"In Progress","summary":"Extensible parameter solution substituting new env variables definition","type":{"description":"A new feature of the product, which has yet to be developed.","name":"New Feature","iconUrl":"/images/icons/issuetypes/newfeature.png"}},{"id":27328,"key":"HSSFTIMP-25","status":"In Progress","summary":"Align Rulesets","type":{"description":"An improvement or enhancement to an existing feature or task.","name":"Improvement","iconUrl":"/images/icons/issuetypes/improvement.png"}},{"id":23170,"key":"HSSFTIMP-14","status":"In Progress","summary":"UnitAttributes for compilation is not having the correct Uses relations","type":{"description":"A problem which impairs or prevents the functions of the product.","name":"Bug","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":19173,"key":"HSSFTIMP-6","status":"In Progress","summary":"SM testSuites provisioning f_cleanDb,   tc:s executed with left over traffic data","type":{"description":"A trouble report imported from MHWEB.","name":"TR","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":18729,"key":"HSSFTIMP-3","status":"In Progress","summary":"Better and fail safe deprovisioning so that database is clean for next test case. ","type":{"description":"An improvement or enhancement to an existing feature or task.","name":"Improvement","iconUrl":"/images/icons/issuetypes/improvement.png"}},{"id":31042,"key":"HSSFTC-218","status":"In Progress","summary":"Fix the current warning in TTCN code","type":{"description":"A problem which impairs or prevents the functions of the product.","name":"Bug","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":30887,"key":"HSSFTC-216","status":"In Progress","summary":"Study the use of the new titan features","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":30540,"key":"HSSFTC-211","status":"In Progress","summary":"Remove monolithic deployment from FT code","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":29640,"key":"HSSFTC-200","status":"In Progress","summary":"Analyse the TS: ts_hsstaf_userLocState_retrieval_NotifEff","type":{"description":"An improvement or enhancement to an existing feature or task.","name":"Improvement","iconUrl":"/images/icons/issuetypes/improvement.png"}},{"id":29340,"key":"HSSFTC-196","status":"In Progress","summary":"Improve/Simplify CFG Files","type":{"description":"A problem which impairs or prevents the functions of the product.","name":"Bug","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":27786,"key":"HSSFTC-166","status":"In Progress","summary":"Review reported CAs in Jenkins","type":{"description":"A problem which impairs or prevents the functions of the product.","name":"Bug","iconUrl":"/images/icons/issuetypes/bug.png"}},{"id":27602,"key":"HSSFTC-165","status":"In Progress","summary":"Test Suites No migrated to CBA","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":25595,"key":"HSSFTC-116","status":"In Progress","summary":"Check NETCONF test case coverage for ExtDb","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":24856,"key":"HSSFTC-76","status":"In Progress","summary":"Check NETCONF test case coverage for SM module","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":24807,"key":"HSSFTC-69","status":"In Progress","summary":"Introduce the Titanium analysis in the CI mechanism","type":{"description":"The sub-task of the issue","name":"Sub-task","iconUrl":"/images/icons/issuetypes/subtask_alternate.png"}},{"id":24052,"key":"HSSFTC-41","status":"In Progress","summary":"FST: Review the coverage of the NETCONF","type":{"description":"An improvement or enhancement to an existing feature or task.","name":"Improvement","iconUrl":"/images/icons/issuetypes/improvement.png"}},{"id":23790,"key":"HSSFTC-29","status":"In Progress","summary":"Define FTStrategy on OSC (How to work in OSC for CBA and TSP) (TASK FORCE)","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":23509,"key":"HSSFTC-22","status":"In Progress","summary":"HSS Virtualization study","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":23363,"key":"HSSFTC-17","status":"In Progress","summary":"HSS FT Auditory 2016","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":23282,"key":"HSSFTC-11","status":"In Progress","summary":"FT056: Use the Titanium plugin in Eclipse for increase TTCN code quality","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}},{"id":31626,"key":"HSSESTINT-85","status":"In Progress","summary":"PoC combined Jumpstarts BSP/HSS","type":{"description":"An improvement or enhancement to an existing feature or task.","name":"Improvement","iconUrl":"/images/icons/issuetypes/improvement.png"}},{"id":31221,"key":"HSSESTINT-84","status":"In Progress","summary":"Check the script for changing PLs floating to Fixed","type":{"description":"A change requested in the deliverables","name":"Deliverable Change Request","iconUrl":"/secure/viewavatar?size=xsmall&avatarId=11000&avatarType=issuetype"}},{"id":30623,"key":"HSSESTINT-76","status":"In Progress","summary":"Test new installation package in VNF37 POD-X","type":{"description":"A task that needs to be done.","name":"Task","iconUrl":"/images/icons/issuetypes/task.png"}}],"title":"","total":166,"url":"","columns":["issuetype","issuekey","summary","assignee","reporter","priority","status","resolution","created","updated","duedate","customfield_10803","labels","customfield_10805"],"columnConfig":"USER"},"warnings":[]}
    # search = Utility.convert_to_string(dict1)
    # #search = '"project"+in+(CHNAPSS)+and+status+in+("Open",Closed,"Preliminary Analysis")+and+"Product Name"+in+(SDM845.LA.1.0)+&maxResults=1&startAt=0'.replace(' ','%20')
    # a,b,c = qurey(search=search)
    # print time.time()
    # a,b,c = qurey(search=search)
    # print time.time()
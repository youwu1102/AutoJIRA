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
A
    url = 'https://jira-cstm.qualcomm.com/jira/rest/api/2/search?jql='
    search = '"project"+in+(CHNAPSS)+and+status+in+("Open",Closed,"Preliminary Analysis")+and+"Product Name"+in+(SDM845.LA.1.0)+&maxResults=1&startAt=0'
    a = urllib.quote('search')
    b = search.replace(' ', '%20')
    #req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/rest/api/2/search?jql=project+in+(CHNAPSS)+and+status+in+(Closed)+&maxResults=1&startAt=0')
    req = urllib2.Request(url + b)
    print req.get_full_url()
    req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (GlobalVariable.account, GlobalVariable.password))[:-1])
    response = urllib2.urlopen(req)
    print response.read()


def qurey(search, start):
    basic_url = 'https://jira-cstm.qualcomm.com/jira/rest/api/2/search?jql='
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
    req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/')
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
    dict1 = {'filter': [['"project" in ("CHNAPSS")', '"status" in ("Open","Closed")'],
                ['"project" in ("CHNAPSS")', '"assignee" in ("c_youwu")']], 'order': u'ASC:Key',
     'display': [u'Key', u'Summary', u'Reporter', u'Status']}
    search = Utility.convert_to_string(dict1)
    #search = '"project"+in+(CHNAPSS)+and+status+in+("Open",Closed,"Preliminary Analysis")+and+"Product Name"+in+(SDM845.LA.1.0)+&maxResults=1&startAt=0'.replace(' ','%20')
    a,b,c = qurey(search=search)
    print time.time()
    a,b,c = qurey(search=search)
    print time.time()
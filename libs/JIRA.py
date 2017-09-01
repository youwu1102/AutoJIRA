__author__ = 'c_youwu'
import urllib2
from base64 import encodestring
import json
import cookielib
import os

class JIRA(object):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__base_url = 'https://jira-cstm.qualcomm.com/jira/rest/api/2/issue/'
        self.__cookie = cookielib.LWPCookieJar()
        self.__opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookie))

        self.data={
            "fields": {
                "project": {
                  "key": "CHNAPSS"
                },
                "summary": "JIRA summary",
                "description": "Just a test for JIRA API",
                "issuetype": {
                  "name": "Bug"
                },
                "customfield_10102": {
                  "value": "Critical"
                },
                "customfield_21339": {
                  "value": "MSM8939.LA.1.1"
                },
                "customfield_21324": "\\\\dine\\CHPDT",
                "customfield_11746": {
                  "value": "PDT CHN"
                },
                "customfield_10456": {
                  "value": "Pre-FC"
                },
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

    def aaa(self):
        self.__cookie = cookielib.LWPCookieJar()
        self.__opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookie))
        urllib2.install_opener(self.__opener)
        req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/rest/api/2/search?jql=project+in+(CHNAPSS)+and+reporter=c_youwu&maxResults=1&startAt=0')
        req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (self.__username, self.__password))[:-1])
        response = urllib2.urlopen(req)
        print response.read()

    def get(self):
        print self.post(self.data)

    def post(self, data):
        url='https://jira-cstm-tools.qualcomm.com/jira/rest/api/2/issue'
        # with open ('C:\Users\c_youwu\Desktop\jira\JiraTemplate.txt') as r:
        #     self.data= r.read()
        print self.data
        print data
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic %s' % encodestring('%s:%s' % (self.__username, self.__password))[:-1],
            'Accept':'*/*'
        }
        request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
        response = urllib2.urlopen(request)
        return response.read()

    def authorization(self):
        # self.__cookie = cookielib.LWPCookieJar()
        # self.__opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookie))
        # urllib2.install_opener(self.__opener)
        req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/')
        req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (self.__username, self.__password))[:-1])
        try:
            urllib2.urlopen(req)
            return 'Success'
        except urllib2.HTTPError:
            return 'Authorization Fail'
        except urllib2.URLError:
            return 'Connection Fail'


    def tmp(self):
        with open('C:\Users\c_youwu\PycharmProjects\AutoJIRA\\tmp.txt') as r:
            str = r.read()
            str = str.replace('null','None')
            str = str.replace('false', 'False')
            str = str.replace('true', 'True')

        dict_str = eval(str)
        issue = dict_str.get('issues')[0]
        print issue



if __name__ == '__main__':
    import time
    jira = JIRA('c_youwu', 'Lct`12`12')
    print time.time()
    print jira.authorization()
    print jira.aaa()
    print time.time()
    # import time
    # print jira.aaa()
    # for x in range(3600):
    #     time.sleep(1)
    #     print x
    #print jira.tmp()

    #print jira.get()

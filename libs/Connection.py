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
        #self.__base_url = 'jira-cstm.qualcomm.com/'
        #String targetUrl = "";
        # private static String IssueBaseURL = "";
        with open('C:\Users\c_youwu\Desktop\jira\JiraTemplate.txt') as r:
            A = r.read()
        self.data = eval(A)
    def aaa(self):
        self.__cookie = cookielib.LWPCookieJar()
        self.__opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookie))
        urllib2.install_opener(self.__opener)
        req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/')
        req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (self.__username, self.__password))[:-1])
        response = urllib2.urlopen(req)
        print response.read()

    def get(self):

        print json.dumps(self.data)
        self.__cookie = cookielib.LWPCookieJar()
        self.__opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__cookie))
        headers = {'Content-Type': 'application/json'}
        urllib2.install_opener(self.__opener)
        req = urllib2.Request(self.__base_url,headers=headers, data=json.dumps(data))
        req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (self.__username, self.__password))[:-1])

        response = urllib2.urlopen(req)
        print response.read()
    def curl(self):
        import urllib
        data =urllib.urlencode(self.data)

        cmd ='curl -k -u {username}:{password} -X POST ' \
             '--data {data} -H \"Content-Type: application/json\"  ' \
             'https://jira-cstm.qualcomm.com/jira/rest/api/2/issue/'\
            .format(username=self.__username, password=self.__password, data=data)
        cmd ='curl -k -u c_youwu:Lct`23`23 -X POST --data {\"fields\":{\"summary\": \"JIRA summary\"}} -H \"Content-Type: application/json\"  https://jira-cstm.qualcomm.com/jira/rest/api/2/issue/'
        print cmd

        a,b,c = os.popen3(cmd)
        print b.read()
        print c.read()

    def httpA(self):
        import urllib
        import httplib
        import base64

        params = urllib.urlencode(self.data)
        auth = base64.b64encode('%s:%s' % (self.__username, self.__password))
        print auth
        headers = {"Authorization": "Basic " + auth, 'Content-Type': 'application/json'}
        conn = httplib.HTTPConnection("jira-cstm.qualcomm.com/jira/rest/api/2/issue/")
        #print conn.getresponse().read()
        conn.request("POST", "", params, headers)
        response = conn.getresponse()
        print response.status
        print response.reason

        print response.read()

        print response.read()

if __name__ == '__main__':
    jira = JIRA('c_youwu', 'Lct`12`12')
    jira.aaa()

    #print jira.get()

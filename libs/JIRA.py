import urllib2
from base64 import encodestring
import json
import cookielib
import GlobalVariable
import traceback
import logging

__url_authorization = 'https://udm-hss-jira.rnd.ki.sw.ericsson.se/login.jsp'
__url_search_basic = 'https://udm-hss-jira.rnd.ki.sw.ericsson.se/rest/api/2/search?jql='
__header = dict()


def aaa():
    url = 'https://udm-hss-jira.rnd.ki.sw.ericsson.se/rest/api/2/search?jql='
    search = 'status%20%3D%20"In%20Progress"'
    # a = urllib.quote('search')
    # b = search.replace(' ', '%20')
    # req = urllib2.Request('https://jira-cstm.qualcomm.com/jira/rest/api/2/search?jql=project+in+(CHNAPSS)+and+status+in+(Closed)+&maxResults=1&startAt=0')
    req = urllib2.Request(url + search)
    print req.get_full_url()
    req.add_header('Authorization', 'Basic %s' % encodestring(
        '%s:%s' % (GlobalVariable.account, GlobalVariable.password))[:-1]
                   )
    response = urllib2.urlopen(req)
    print response.read()


def search(**kwargs):
    url = '{basic}{filter}&maxResults={max}&startAt={start}'.format(basic=__url_search_basic,
                                                                    filter=kwargs.get('filter'),
                                                                    max=kwargs.get('max'),
                                                                    start=kwargs.get('start')
                                                                    )
    logging.info("SEARCH: %s" % url)
    return __get(url=url, account=GlobalVariable.account, password=GlobalVariable.password)


def __get(url, account, password):
    # cookie = cookielib.LWPCookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # urllib2.install_opener(opener)
    headers = {'Authorization': 'Basic %s' % encodestring('%s:%s' % (account, password))[:-1]}
    request = urllib2.Request(url=url, headers=headers)
    try:
        response = urllib2.urlopen(request).read()
        return 0, response
    except urllib2.HTTPError:
        return 1, ''
    except urllib2.URLError:
        return 2, ''


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
    req = urllib2.Request(__url_authorization)
    req.add_header('Authorization', 'Basic %s' % encodestring('%s:%s' % (account, password))[:-1])
    try:
        urllib2.urlopen(req)
        logging.info('Success')
        return 0, 'Success'
    except urllib2.HTTPError:
        logging.error(traceback.format_exc())
        return 1, 'Authorization Fail'
    except urllib2.URLError:
        logging.error(traceback.format_exc())
        return 2, 'Connection Fail'


if __name__ == '__main__':
    import time

    print time.time()
    authorization(GlobalVariable.account, GlobalVariable.password)
    print time.time()
    a, b = search(filter='status%20%3D%20\"In%20Progress\"', start=10, max=1)
    print b
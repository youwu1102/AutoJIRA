# -*- encoding:UTF-8 -*-
import threading
from time import sleep
import JIRA
import time
import GlobalVariable
from wx import CallAfter

false = 'false'
true = 'true'
none = 'none'


class ThreadManager(threading.Thread):
    def __init__(self, update, data):
        threading.Thread.__init__(self)
        self.update = update
        self.data = data
        self.work_queue = list()
        self.threads = list()
        self.__cycle_time = 1


    def append_work(self, **kwargs):
        if kwargs not in self.work_queue:
            self.work_queue.append(kwargs)

    def __parse_work(self, **kwargs):
        work_type = kwargs.get('type')
        start = time.time()
        if work_type == 'query':
            print 'query'
            self.data.remove_all_row_data()
            self.__query(**kwargs)
        elif work_type == '':
            self.__a

        elif work_type == 'previous':
            pass
        elif work_type == 'next':
            print 'next'
            self.__next(**kwargs)



        else:
            print 'UNKNOW'
        end = time.time()
        print end - start


    def __query(self, **kwargs):
        start = kwargs.get('start')
        search = kwargs.get('query')
        end = start + GlobalVariable.max_result
        self.data.set_search_string(search)
        code, response, traceback = JIRA.qurey(search=search, start=start)
        if code == 0:
            self.parse_response(response=response)
            self.data.set_data(start=start, end=end)
            CallAfter(self.update, )
            kwargs.get('dialog').stop()
        # 下面代码没有调试过
        elif code == 1:
            JIRA.authorization(account=GlobalVariable.account, password=GlobalVariable.password)
            self.__query(**kwargs)
        elif code == 2:
            print 'Please visit the \'https://jira-cstm.qualcomm.com/\' and check the connection.'

    def __next(self, **kwargs):
        start = self.data.get_current_index()
        query = self.data.get_search_string()
        if query:
            self.__query(query=query, start=start, **kwargs)

    def run(self):
        while True:
            sleep(self.__cycle_time)
            if self.work_queue:
                self.__parse_work(**self.work_queue.pop())
            else:
                sleep(1)

    def set_default_cycle_time(self):
        self.__cycle_time = 1

    def set_cycle_time(self, sec):
        self.__cycle_time = sec

    def parse_response(self, response):
        response = eval(response)
        issues = response.get('issues')
        for issue in issues:
            issue_row = [
                issue.get('key'),
                issue.get('fields').get('status').get('name'),
                issue.get('fields').get('reporter').get('name'),
                issue.get('fields').get('summary')
            ]
            self.data.append_row(issue_row)



if __name__ == '__main__':
    with open('C:\Users\c_youwu\Desktop\\ddd.txt') as r:
        aresponse = r.read()
    ThreadManager.parse_response(response=aresponse)
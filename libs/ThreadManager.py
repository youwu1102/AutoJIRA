# -*- encoding:UTF-8 -*-

import JIRA
import logging
import threading

false = 'false'
true = 'true'
none = 'none'

__thread_pool = dict()


def append_work(**kwargs):
    logging.info("Add new work:")
    logging.info("%s" % kwargs)
    __parse_work(**kwargs)


def __parse_work(**kwargs):
    work_type = kwargs.get('type')
    if work_type in __thread_pool.keys():
        if __thread_pool.get(work_type).isAlive():
            logging.warning("Same work is already in process.")
            logging.warning("Skip")
            return None
    if work_type == "login":
        __append_thread(target=__login, name="login", **kwargs)
    elif work_type == "query":
        __append_thread(target=__query, name="query", **kwargs)
    elif work_type == "previous":
        __append_thread(target=__previous, name="previous", **kwargs)
    elif work_type == "next":
        __append_thread(target=__next, name="next", **kwargs)
    else:
        logging.warning("Unknown work type")


def __append_thread(**kwargs):
    target = kwargs.get("target")
    name = kwargs.get('name')
    t = threading.Thread(target=target, kwargs=kwargs)
    __thread_pool[name] = t
    t.start()


def __login(**kwargs):
    logging.info("start login")
    password = kwargs.get('password')
    account = kwargs.get('account')
    update = kwargs.get('update')
    update("Logging. Please wait …")
    code, response = JIRA.authorization(account=account, password=password)
    if code == 0:
        update(msg=response, level="i")
        kwargs.get('dialog').Destroy()
    elif code == 1:
        update(msg=response, level="e")
    elif code == 2:
        update(msg=response, level="e")


def __query(**kwargs):
    logging.info("start query")
    code, response = JIRA.search(**kwargs)
    if code == 0:
        kwargs.get('dialog').Destroy()
        print response
    elif code == 1:
        update(msg=response, level="e")
    elif code == 2:
        update(msg=response, level="e")

    # clear all data
    #
    pass
    # start = kwargs.get('start')
    # search = kwargs.get('query')
    # end = start + GlobalVariable.max_result
    # self.data.set_search_string(search)
    # code, response, traceback = JIRA.qurey(search=search, start=start)
    # if code == 0:
    #         self.parse_response(response=response)
    #         self.data.set_data(start=start, end=end)
    #         CallAfter(self.update, )
    #         kwargs.get('dialog').stop()
    #     # 下面代码没有调试过
    #     elif code == 1:
    #         JIRA.authorization(account=GlobalVariable.account, password=GlobalVariable.password)
    #         self.__query(**kwargs)
    #     elif code == 2:
    #         print 'Please visit the \'https://jira-cstm.qualcomm.com/\' and check the connection.'

def __next(**kwargs):
    pass
    # start = self.data.get_current_index()
    # query = self.data.get_search_string()
    # if query:
    #     self.__query(query=query, start=start, **kwargs)


def __previous(**kwargs):
    pass
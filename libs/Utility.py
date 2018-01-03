from xml.dom.minidom import Document
from xml.dom.minidom import parse
import traceback
from GlobalVariable import config_folder, dict_query_config
from os.path import join

#import win32clipboard
from os import sep


def convert_to_string(dict_query):

    def convert_filter(filter_):
        filter_list = list()
        for f in filter_:
            f = ['+'.join(x.split(' ')) for x in f]
            filter_list.append('+AND+'.join(f))
        string = '+OR+'.join(filter_list)
        return string.replace(' ', '%20')

    def convert_display(display_):
        display_list = list()
        for d in display_:
            display_list.append(d.lower())
        string = 'fields=' + ','.join(display_list)
        return string.replace(' ', '%20')

    def convert_order_by(order_by):
        order_by = order_by.split(':')
        string = 'ORDER+BY+%s+%s' % (order_by[1].lower(), order_by[0])
        return string.replace(' ', '%20')

    filter_string = convert_filter(dict_query.get('filter'))
    display_string = convert_display(dict_query.get('display'))
    order_string = convert_order_by(dict_query.get('order'))
    search = '{filter}+{order}&{display}'.format(filter=filter_string, display=display_string, order=order_string)
    return search


def parse_config(config_name):
    print config_name
    config_path = join(config_folder, config_name)
    choice_list = list()
    try:
        doc = parse(config_path)
        options = doc.getElementsByTagName('option')
        for option in options:
            choice_list.append(option.getAttribute('value'))
    except Exception:
        print 'Error in parse profile'
        print traceback.format_exc()
    finally:
        return choice_list


def __get_value(root, tag):
    nodes = root.getElementsByTagName(tag)
    for node in nodes:
        rc = ""
        for node in node.childNodes:
            if node.nodeType in ( node.TEXT_NODE, node.CDATA_SECTION_NODE):
                rc = rc + node.data
    return rc

def parse_profile(profile_path):
    profile = dict()
    try:
        doc = parse(profile_path)
        options = doc.getElementsByTagName('option')
        for option in options:
            option_value_list = list()
            values = option.getElementsByTagName('value')
            for value in values:
                if len(value.childNodes) == 0:
                    option_value_list.append('')
                else:
                    option_value_list.append(value.childNodes[0].nodeValue)
            profile[option.getAttribute('name')] = '\n'.join(option_value_list)
    except UnicodeTranslateError:
        print 'Error in parse profile'
    finally:
        return profile


def save_profile(profile_path, profile):
    doc = Document()
    root = doc.createElement('fields')
    for key in profile.keys():
        node = doc.createElement('option')
        node.setAttribute('name', key)
        values = profile.get(key)
        values = values.split('\n')
        for value in values:
            value_E = doc.createElement('value')
            value_T = doc.createTextNode(value)
            value_E.appendChild(value_T)
            node.appendChild(value_E)
        root.appendChild(node)
    doc.appendChild(root)
    with open(profile_path, 'w') as xml:
        xml.write(doc.toprettyxml(indent='\t', encoding='utf-8'))


def send_to_clipboard(value):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_TEXT, str(value))
    win32clipboard.CloseClipboard()

def path_join(path, *paths):
    return join(path, *paths)

def __parse_condition(condition):
    f = condition.getAttribute('FIELD')
    e = condition.getAttribute('EXPRESSION')
    v = condition.getAttribute('VALUE')
    values = v.split('|')
    if e == 'in':
        values = ['\"%s\"' % x for x in values]
        value = ','.join(values)
        return '{filed} in ({value})'.format(filed='\"%s\"' % f, value=value)


def __parse_by(by):
    f = by.getAttribute('FIELD')
    s = by.getAttribute('SORT')
    if s.lower() == "desc":
        return 'DESC:%s' % f
    else:
        return 'ASC:%s' % f

def parse_query(query_path):
    query = dict()
    try:
        doc = parse(query_path)
        root = doc.documentElement
        _filter = root.getElementsByTagName('FILTER')[0]
        _display = root.getElementsByTagName('DISPLAY')[0]
        _order = root.getElementsByTagName('ORDER')[0]
        _rules = _filter.getElementsByTagName('RULE')
        filter_list = list()
        for _rule in _rules:
            rule_list = list()
            _conditions = _rule.getElementsByTagName('COND')
            for _condition in _conditions:
                rule_list.append(__parse_condition(_condition))
            filter_list.append(rule_list)
        _fields = _display.getElementsByTagName('FIELD')
        display_list = list()
        for field in _fields:
            display_list.append(field.childNodes[0].nodeValue)
        _by = _order.getElementsByTagName('BY')[0]
        order_ = __parse_by(by=_by)
        query['order'] = order_
        query['display'] = display_list
        query['filter'] = filter_list
    except UnicodeTranslateError:
        print 'Error in parse query'
    finally:
        return query


def append_tree(tree, root, query):
    def append_filter(node, filter_):
        def append_condition(and_node, condition):
            tree.AppendItem(and_node, condition)
        node = tree.AppendItem(node, 'Filter')
        if len(filter_) == 1:
            and_node = tree.AppendItem(node, 'AND')
            for condition in filter_[0]:
                append_condition(and_node=and_node, condition=condition)
        elif len(filter_) == 0:
            print 'FILTER ERROR'
            return
        else:
            or_node = tree.AppendItem(node,'OR')
            for f in filter_:
                and_node = tree.AppendItem(or_node, 'AND')
                for condition in f:
                    append_condition(and_node=and_node,condition=condition)

    def append_display(node, display_):
        node = tree.AppendItem(node, 'Display')
        for d in display_:
            tree.AppendItem(node, d)

    def append_order(node, order_):
        node = tree.AppendItem(node, 'Order')
        tree.AppendItem(node, order_)



    dict_query = parse_query(query_path=query)
    query_name = query.split(sep)[-1][:-4]
    dict_query_config[query_name] = dict_query
    if {}:
        print 'TREE ERROR'
        return
    query_node = tree.AppendItem(root, query_name)
    append_filter(query_node, dict_query.get('filter'))
    append_display(query_node, dict_query.get('display'))
    append_order(query_node, dict_query.get('order'))




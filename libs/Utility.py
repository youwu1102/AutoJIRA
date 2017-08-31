from xml.dom.minidom import Document
from xml.dom.minidom import parse


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

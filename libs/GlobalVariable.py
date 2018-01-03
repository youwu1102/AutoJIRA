import sys
from os.path import join, abspath, dirname
from time import strftime, localtime
from libs.ui.GridData import GridData
dict_query_config = dict()
account = 'zyouwux'
password = 'Lct123123'
work_dir = abspath(dirname(sys.argv[0]))
log_folder = join(work_dir, 'log')
resource_folder = join(work_dir, 'resource')
config_folder = join(resource_folder, 'config')
query_folder = join(resource_folder, 'query')
template_folder = join(resource_folder, 'template')

issue_default_profile = join(template_folder, 'default.xml')

default_log_path = join(log_folder, '%s.log' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))

grid_data = GridData()



icon_import = join(resource_folder, 'icon', 'import.png')
icon_export = join(resource_folder, 'icon', 'export.png')
icon_save = join(resource_folder, 'icon', 'save.png')


max_result = 100
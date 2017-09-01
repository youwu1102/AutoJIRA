from os.path import join

account = ''
password = ''

work_dir = 'C:\Users\c_youwu\PycharmProjects\AutoJIRA'
resource_folder = join(work_dir, 'resource')
config_folder = join(resource_folder, 'config')
template_folder = join(resource_folder, 'template')
issue_default_profile = join(template_folder, 'default.xml')

icon_import = join(resource_folder, 'icon', 'import.png')
icon_export = join(resource_folder, 'icon', 'export.png')
icon_save = join(resource_folder, 'icon', 'save.png')
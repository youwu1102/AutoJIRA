import os
path = 'C:\Users\c_youwu\Documents\GitHub\APT_KPI_Tools'
def find(path):
    folders = os.listdir(path)
    for folder in folders:
        folder_path = os.path.join(path,folder)
        if os.path.isdir(folder_path):
            print folder_path
            find(folder_path)
        else:
            if folder.endswith('.java'):
                with open(folder_path) as r:
                    for line in r.readlines():
                        if 'get(' in line:
                            print folder_path
                            print line
find(path)
w_file = open('1.txt','w')
with open ('C:\Users\c_youwu\Desktop\\22\logcat.txt') as r:
    for line in r.readlines():
        try:
            w_file.write(line[line.index(': ')+2:].strip('\n'))
        except Exception:
            w_file.write(line.strip('\r\n') + '\n')
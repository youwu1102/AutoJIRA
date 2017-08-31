with open ('C:\Users\c_youwu\Desktop\ddd.txt') as r:
    for line in r.readlines():
        line = line.strip('\r\n').lstrip(' ')
        #print line
        profile = line[ line.index('(profile'):].replace('(profile.get(', 'profile[').replace('(ic.name)))','(ic.name)]')
        v = line[ :line.index('(profile')].replace('SetStringSelection', 'GetStringSelection').replace('SetValue','GetValue')+'()'
        print profile +' = '+v


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print 'Parent'

    def bar(self, message):
        print message, 'from Parent'


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print 'Child'

    def bar(self, message):
        super(FooChild, self).bar(message)
        print 'Child bar fuction'
        print self.parent


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')


import wx
import time
if __name__ == "__msain__":
    app = wx.App()
    progressMax = 100
    dialog = wx.ProgressDialog("A progress box", "Wait for data", progressMax,
            style=wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
    keepGoing = True
    count = 0
    while True:
        if count < progressMax:
            count += 3
        print time.time()
        time.sleep(0.1)
        print time.time()
        print 's'
        keepGoing = dialog.Update(count)

    print 's'
    #dialog.Destroy()
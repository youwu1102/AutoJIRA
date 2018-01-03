# -*- encoding:UTF-8 -*-
import wx


class ProgressDialog(wx.Dialog):
    def __init__(self, seconds, title, message, timeout=10):
        wx.Dialog.__init__(self, None, -1, title=title, size=(300, 150))
        self.Center()
        panel = wx.Panel(self)
        self.__message_text = wx.StaticText(panel, -1, pos=(20, 20), label=message)
        self.__info_text = wx.StaticText(panel, -1, pos=(20, 50), label="")
        self.__unit = 1000 / seconds
        self.__count = 0
        self.__gauge = wx.Gauge(panel, -1, 10000, (20, 80), (250, 25))
        self.__gauge.SetBezelFace(3)
        self.__gauge.SetShadowWidth(3)
        self.__stop_flag = False
        self.__time_interval = 100
        self.__timer_count = 0
        self.__timeout = timeout * 1000
        self.__timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.__on_timer, self.__timer)
        self.__timer.Start(self.__time_interval)
        self.Bind(wx.EVT_CLOSE, self.__on_close)

    def __on_close(self, event):
        if self.__timer_count > self.__timeout:
            self.Destroy()
        else:
            self.__info_text.SetLabel('Please wait until it complete')

    def __on_timer(self, evt):
        if not self.__stop_flag:

            self.__timer_count += self.__time_interval


            if self.__count == -1:
                pass
            elif 9800 <= self.__count + self.__unit <= 10000:
                self.__gauge.SetValue(9850)
                self.__count = -1
            else:
                self.__count += self.__unit
                self.__gauge.SetValue(self.__count)
        else:
            self.Destroy()

    def stop(self):
        self.__stop_flag = True


if __name__ == '__main__':
    app = wx.App()
    login = ProgressDialog(2, title='sss',  message='ddd')
    login.Show()
    app.MainLoop()

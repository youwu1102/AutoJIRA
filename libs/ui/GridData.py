import wx.grid


class GridData(wx.grid.PyGridTableBase):
    __rows = []
    __index = 0
    __query = ''
    _cols = []
    _data = []

    _highlighted = set()

    def GetColLabelValue(self, col):
        return self._cols[col]

    def GetNumberRows(self):
        return len(self._data)

    def GetNumberCols(self):
        return len(self._cols)

    def GetValue(self, row, col):
        return self._data[row][col]

    def append_row(self, row):
        self.__rows.append(row)

    def remove_all_row_data(self):
        self.__rows = []

    def set_data(self, start, end):
        self.__index = end
        self._data = self.__rows[start:end]

    def set_search_string(self, string):
        self.__query = string

    def get_search_string(self):
        return self.__query

    def get_current_index(self):
        return self.__index

    def reset_cols(self,cols):
        self._cols =cols


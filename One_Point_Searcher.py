


class OnePointSearcher:


    def __init__(self, dataRecorder, field, pollutionReader):
        self.__dataRecorder = dataRecorder
        self.__field = field
        self.__pollutionReader = pollutionReader


    def Search(self, x, y, t):

        self.__CanSearch(x, y, t)
        pollution = self.__MeasurePollution(x, y, t)
        self.__RecordDatas(x, y, t, pollution)

        return x, y, t, pollution


    def __IsInSearchableArea(self, x, y, t):
        isSearchable = x >= self.__field.GetLowerX() and \
                       x <= self.__field.GetUpperX() and \
                       y >= self.__field.GetLowerY() and \
                       y <= self.__field.GetUpperY() and \
                       t >= self.__field.GetLowerT() and \
                       t <= self.__field.GetUpperT()

        return isSearchable



    def __IsInt(self, x, y):
        isInt = ((type(x) == int) and (type(y) == int))
        if(not isInt):
            raise ValueError('探索座標は整数にしてください')


    def __CanSearch(self, x, y, t):
        isSearchable = self.__IsInSearchableArea(x, y, t)
        if(not isSearchable):
            raise ValueError('探索不可能座標もしくは不可能時間です')

        self.__IsInt(x, y)

    def __RecordDatas(self, x, y, t, pollution):
        self.__dataRecorder.Append(x, y, t, pollution)

    def __MeasurePollution(self, x, y, t):
        pollution = self.__pollutionReader.Read(x, y, t)
        return pollution

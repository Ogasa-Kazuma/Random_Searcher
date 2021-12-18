


class OnePointSearcher:


    def __init__(self, dataRecorder, field):
        self.__dataRecorder = dataRecorder
        self.__field = field


    def Search(self, x, y, speed):

        self.__CanSearch(x, y)

        self.__RecordData(x, y, speed)
        pollution = self.__MeasurePollution()

        return pollution


    def __IsInSearchableArea(self, x, y):
        isSearchable = x >= self.__field.GetLowerX() and \
                       x <= self.__field.GetUpperX() and \
                       y >= self.__field.GetLowerY() and \
                       y <= self.__field.GetUpperY()

        return isSearchable



    def __IsInt(self, x, y):
        isInt = ((type(x) == int) and (type(y) == int))
        if(not isInt):
            raise ValueError('探索座標は整数にしてください')


    def __CanSearch(self, x, y):
        isSearchable = self.__IsInSearchableArea(x, y)
        if(not isSearchable):
            raise ValueError('探索不可能領域です')

        self.__IsInt(x, y)

    def __RecordData(self, x, y, speed):
        self.__dataRecorder.Append(dict(x = x, y = y, speed = speed))

    def __MeasurePollution(self):
        pollution = self.__dataRecorder.GetLatestPollution()
        return pollution

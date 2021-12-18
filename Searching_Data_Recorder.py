
# -*- coding: utf-8 -*-

import numpy as np

class SearchingDataRecorder:
    """探索した場所と、その時間を一時的に記録するクラス"""


    def __init__(self, pollutionReader):

        self.__pollutionReader = pollutionReader

        self.__x = list()
        self.__y = list()
        self.__t = list()
        self.__pollution = list()

    def Append(self, kwargs):

        x, y, speed = kwargs['x'], kwargs['y'], kwargs['speed']

        self.__x.append(x)
        self.__y.append(y)

        t = self.__CalcTime(speed)
        self.__t.append(t)

        pollution = self.__pollutionReader.Read(x, y, t)

        self.__pollution.append(pollution)

        return self.__x[-1], self.__y[-1], self.__t[-1], self.__pollution[-1]


    def GetLatestTime(self):
        return self.__t[-1]

    def GetPositions(self):
        return self.__x, self.__y

    def GetAllData(self):
        return self.__x, self.__y, self.__t, self.__pollution


    def __IsZeroTime(self):
        result = len(self.__x) < 2 or len(self.__y) < 2
        return result


    def __CalcTime(self, speed):

        #開始0秒の時点
        if(self.__IsZeroTime()):
            return 0

        distance = self.__CalcDistance()

        t_inc = distance / speed

        t = self.__t[-1] + t_inc

        return t





    def __CalcDistance(self):

        x_calc = (self.__x[-1] - self.__x[-2] ) ** (2)
        y_calc = (self.__y[-1] - self.__y[-2] ) ** (2)
        distance = np.sqrt(x_calc + y_calc)

        return distance

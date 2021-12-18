# -*- coding: utf-8 -*-
import glob
import pandas as pd
import math
import re

class PollutionReader:

    def __init__(self, dirPath, format, fileReader):
        self.__dirPath = dirPath
        self.__format = '.' + self.__RemoveExpectAlphabet(format)
        self.__fileReader = fileReader

    def SetDir(self, dirPath):
        self.__dirPath = dirPath

    def SetFormat(self, format):
        self.__format = '.' + str(format)

    def Read(self, x, y, t):

        #切り上げ、切り捨て
        t_down = self.__RoundDown(t)
        t_up = self.__RoundUp(t)

        file_down = self.__SpecifyFile(t_down)
        file_up = self.__SpecifyFile(t_up)

        pollution_down = self.__ReadPollution(file_down, x, y)
        pollution_up = self.__ReadPollution(file_up, x, y)

        #線形補完
        pollution = self.__LinearInterpolation(t, pollution_down, pollution_up, t_down, t_up)

        return pollution


    def __RemoveExpectAlphabet(self, string):
        string = self.__ToString(string)
        string = re.sub(r"[^a-zA-Z]", "", string)
        return string



    def __ToString(self, string):
        return str(string)


    def __RoundUp(self, value):
        value = math.ceil(value)
        return value

    def __RoundDown(self, value):
        value = math.floor(value)
        return value


    def __SpecifyFile(self, t):
        fileLocation = self.__dirPath + str(t) + self.__format
        files = glob.glob(fileLocation, recursive=True)

        file = files[0]

        return file



    def __ReadPollution(self, path, x, y):

        file = self.__fileReader.Read(path)

        count = file['y'][0] * x + y
        concent = file['pollutions'][count]

        return concent


    def __LinearInterpolation(self, t, pollution_down, pollution_up, t_down, t_up):

        diff_pollution = pollution_up - pollution_down
        diff_t = t_up - t_down

        #整数値の時間が入力されたら線形補完の必要なし
        if(not diff_t):
            return pollution_down

        #濃度変化と時間の変化割合
        ratio = diff_pollution / diff_t

        #tの小数点部分のみ計算
        t_offset = t - t_down

        pollution_change = ratio * t_offset
        pollution = pollution_down + pollution_change

        return pollution

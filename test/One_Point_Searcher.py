
# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import importlib

import Searching_Data_Recorder
import Pollution_Reader
import Pickle_Reader
import Field
import One_Point_Searcher

importlib.reload(Searching_Data_Recorder)
importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)
importlib.reload(Field)
importlib.reload(One_Point_Searcher)



def main():

    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    dataRecorder = Searching_Data_Recorder.SearchingDataRecorder(pollutionReader)
    field = Field.FieldClass(dict(uprX = 99, uprY = 99, uprT = 2999, lwrX = 0, lwrY = 0, lwrT = 0))
    onePointSearcher = One_Point_Searcher.OnePointSearcher(dataRecorder, field)

    #x, yに小数を入力しても動作してしまう
    print(onePointSearcher.Search(30, 80, speed = 20))
    print(onePointSearcher.Search(30, 81, speed = 1))

    print(pollutionReader.Read(30, 81, 1))

if __name__ == "__main__":
    main()

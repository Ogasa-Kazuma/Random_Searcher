
# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import importlib

import Searching_Data_Recorder
import Data_Recorder
import Pollution_Reader
import Pickle_Reader
import Field
import One_Point_Searcher
import Straight_Line_Searcher
import Time_Limitter

importlib.reload(Searching_Data_Recorder)
importlib.reload(Data_Recorder)
importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)
importlib.reload(Field)
importlib.reload(One_Point_Searcher)
importlib.reload(Straight_Line_Searcher)
importlib.reload(Time_Limitter)


def main():

    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    dataRecorder = Data_Recorder.DataRecorder()
    field = Field.FieldClass(dict(uprX = 99, uprY = 99, uprT = 2999, lwrX = 0, lwrY = 0, lwrT = 0))
    onePointSearcher = One_Point_Searcher.OnePointSearcher(dataRecorder, field, pollutionReader)

    lineSearcher = Straight_Line_Searcher.StraightLineSearcher(onePointSearcher)
    print(lineSearcher.Search(dict(threshold = 90, x1 = 50, x2 = 70, y1 = 50, y2 = 70, start_time = 0, max_time = -1, speed = 1)))
    print(lineSearcher.Search(dict(threshold = 90, x1 = 10, x2 = 0, y1 = 70, y2 = 0, start_time = 1, max_time = 2, speed = 20)))
    print(lineSearcher.Search(dict(threshold = 90, x1 = 10, x2 = 0, y1 = 70, y2 = 0, start_time = 0, max_time = 200, speed = 1)))
    print(lineSearcher.Search(dict(threshold = 90, x1 = 10, x2 = 0, y1 = 70, y2 = 0, start_time = 0, max_time = 200, speed = 1)))


if __name__ == "__main__":
    main()

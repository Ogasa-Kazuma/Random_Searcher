

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
import Random_Move_Searcher

importlib.reload(Searching_Data_Recorder)
importlib.reload(Data_Recorder)
importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)
importlib.reload(Field)
importlib.reload(One_Point_Searcher)
importlib.reload(Straight_Line_Searcher)
importlib.reload(Time_Limitter)
importlib.reload(Random_Move_Searcher)

def main():

    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    dataRecorder = Data_Recorder.DataRecorder()
    field = Field.FieldClass(dict(uprX = 99, uprY = 99, uprT = 2999, lwrX = 0, lwrY = 0, lwrT = 0))
    onePointSearcher = One_Point_Searcher.OnePointSearcher(dataRecorder, field, pollutionReader)

    lineSearcher = Straight_Line_Searcher.StraightLineSearcher(onePointSearcher)
    randomMoveSearcher = Random_Move_Searcher.RandomMoveSearcher(dataRecorder, lineSearcher)
    print(randomMoveSearcher.Search(start_x = 50,\
                                    start_y = 50,\
                                    start_time = 10,\
                                    max_time = 1500,\
                                    max_x = 99,\
                                    max_y = 99,\
                                    min_x = 0,\
                                    min_y = 0,\
                                    speed = 2,\
                                    threshold = 80))

    print(pollutionReader.Read(56, 63, 30.5))

if __name__ == "__main__":
    main()

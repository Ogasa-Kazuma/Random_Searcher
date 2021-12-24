
# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import importlib
import numpy as np

import Next_Direction_Chooser
import Linear_Function
import Linear_Function_Ret_Int
import Probability_Distribution_Creater
import Searching_Data_Recorder
import Data_Recorder
import Pollution_Reader
import Pickle_Reader
import Field
import One_Point_Searcher
import Straight_Line_Searcher
import Surrounding_Searcher
import Params
import Coordinate_Calculator
import Random_Searcher
import Time_Limitter
import Random_Move_Searcher

importlib.reload(Next_Direction_Chooser)
importlib.reload(Linear_Function)
importlib.reload(Linear_Function_Ret_Int)
importlib.reload(Probability_Distribution_Creater)
importlib.reload(Searching_Data_Recorder)
importlib.reload(Data_Recorder)
importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)
importlib.reload(Field)
importlib.reload(One_Point_Searcher)
importlib.reload(Straight_Line_Searcher)
importlib.reload(Surrounding_Searcher)
importlib.reload(Params)
importlib.reload(Coordinate_Calculator)
importlib.reload(Random_Searcher)
importlib.reload(Time_Limitter)
importlib.reload(Random_Move_Searcher)


def main():

    #第1 注入オブジェクト
    coordinateCalculator = Coordinate_Calculator.CoordinateCalculator()

    #第2　注入オブジェクト
    func = Linear_Function.LinearFunction(maxValue = 100, maxPoint = 0, zeroPoint = 180)
    distCalculator = Linear_Function_Ret_Int.LinearFunctionRetInt(func)
    distMaker = Probability_Distribution_Creater.Degrees_Distribution_Creater(distCalculator)
    chooser = Next_Direction_Chooser.NextDirectionChooser(distMaker)

    #第3 注入オブジェクト
    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    dataRecorder = Data_Recorder.DataRecorder()
    field = Field.FieldClass(dict(uprX = 99, uprY = 99, uprT = 2999, lwrX = 0, lwrY = 0, lwrT = 0))
    onePointSearcher = One_Point_Searcher.OnePointSearcher(dataRecorder, field, pollutionReader)
    lineSearcher = Straight_Line_Searcher.StraightLineSearcher(onePointSearcher)

    #第4注入オブジェクト
    params = Params.ParamsClass(dict(distElements = np.arange(-180.0, 180.0, 0.1), excludeDegreeWidth = 30))


    # 本体1

    surroundingSearcher = Surrounding_Searcher.SurroundingSearcher(chooser, lineSearcher, coordinateCalculator, params)



    randomMoveSearcher = Random_Move_Searcher.RandomMoveSearcher(dataRecorder, lineSearcher)





    randomSearcher = Random_Searcher.RandomSearcher(surroundingSearcher, randomMoveSearcher)
    print(randomSearcher.Search(start_time              = 0,\
                          max_time                      = 200,\
                          start_x                       = 50,\
                          start_y                       = 50,\
                          max_random_x                  = 99,\
                          max_random_y                  = 99,\
                          min_random_x                  = 0,\
                          min_random_y                  = 0,\
                          firstDirection                = 90,\
                          threshold                     = 10,\
                          speed                         = 2,\
                          maxStraightLineSearchDistance = 10\
                          ))

    print(dataRecorder.GetAllData())

if __name__ == "__main__":
    main()

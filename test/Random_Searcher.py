
# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import importlib
import matplotlib.pyplot as plt
import numpy as np
import copy

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
import class_pollution_state_drawer_2D

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
importlib.reload(class_pollution_state_drawer_2D)


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
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/", "pkl", pklReader)
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
    print(randomSearcher.Search(start_time              = 1000,\
                          max_time                      = 1150,\
                          start_x                       = 50,\
                          start_y                       = 50,\
                          max_random_x                  = 99,\
                          max_random_y                  = 99,\
                          min_random_x                  = 0,\
                          min_random_y                  = 0,\
                          firstDirection                = 315,\
                          threshold                     = 10,\
                          speed                         = 2,\
                          maxStraightLineSearchDistance = 30\
                          ))

###############################################################################
    #/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/1日/16時/20分/13秒
    #/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/
    path = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/1日/16時/20分/13秒/" + str(0) + ".pkl"
    pollutionLog = pklReader.Read(path)
    plns = copy.deepcopy(pollutionLog["pollutions"])
    plns = plns.values.tolist()
    maxPln = max(plns)

    for i in range(len(plns)):
        plns[i] = plns[i] / maxPln


    xlim = int(pollutionLog["x"][0])
    ylim = int(pollutionLog["y"][0])
    first_t = int(pollutionLog["start_t"][0])
    last_t = int(pollutionLog["end_t"][0])

    new_x = list()
    new_y = list()




    for x_i in range(0, xlim, 1):
        for y_i in range(0, ylim, 1):

            new_x.append(x_i)
            new_y.append(y_i)





    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.scatter(new_x, new_y, s= 20,  c = plns, cmap = 'binary')
################################################################

    x, y, t, pollutions = dataRecorder.GetAllData()
    ax.scatter(x, y, s = 5, c = 'red')
    plt.show()
    savePath = "../PollutionCreate/Pic_Pollution/thesis/" + "dynamic_method_" + "len30_deg315" + ".png"
    fig.savefig(savePath)


if __name__ == "__main__":
    main()

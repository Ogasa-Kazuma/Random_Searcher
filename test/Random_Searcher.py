
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
import Pollution_Data_Reshaper
import Saved_Pollution_Indexs


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
importlib.reload(Pollution_Data_Reshaper)
importlib.reload(Saved_Pollution_Indexs)




def ExcludeOverTime(max_time, dataRecorder):
    x, y, t, pollutions = dataRecorder.GetAllData()
    new_x = list()
    new_y = list()
    for i in range(len(x)):
        if(t[i] <= max_time):
            new_x.append(x[i])
            new_y.append(y[i])

    return new_x, new_y



def PrintSearchingMoment(fileDir, indexNames, pollutionReshaper, dataRecorder, start_t, end_t):
    for t_i in range(start_t, end_t, 10):
        path = fileDir + str(t_i) + ".pkl"
        draw_x, draw_y, pollutions = pollutionReshaper.Reshape(path, indexNames)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.set_xlabel("x [m]")
        ax.set_ylabel("y [m]")
        ax.scatter(draw_x, draw_y, s= 20,  c = pollutions, cmap = 'binary')
    ################################################################
        x, y = ExcludeOverTime(max_time = t_i, dataRecorder = dataRecorder)
        ax.plot(x, y, c = 'blue', linewidth = 1)
        plt.show()
        savePath = "../PollutionCreate/Pic_Pollution/" + str(t_i)  + ".png"
        fig.savefig(savePath, dpi = 300)






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



    randomMoveSearcher = Random_Move_Searcher.RandomMoveSearcher(lineSearcher)




    randomSearcher = Random_Searcher.RandomSearcher(surroundingSearcher, randomMoveSearcher)
    print(randomSearcher.Search(start_time              = 1000,\
                          max_time                      = 1150,\
                          start_x                       = 99,\
                          start_y                       = 99,\
                          max_random_x                  = 99,\
                          max_random_y                  = 99,\
                          min_random_x                  = 0,\
                          min_random_y                  = 0,\
                          firstDirection                = 275,\
                          threshold                     = 10,\
                          speed                         = 2,\
                          maxStraightLineSearchDistance = 30\
                          ))

###############################################################################
    #/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/1日/16時/20分/13秒
    #/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/


    fileDir = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/1日/16時/20分/13秒/"
    indexNames = Saved_Pollution_Indexs.SavedPollutionIndexs("pollutions", "x", "y")
    pollutionReshaper = Pollution_Data_Reshaper.PollutionDataReshaper(pklReader)

    PrintSearchingMoment(fileDir, indexNames, pollutionReshaper, dataRecorder, start_t = 1000, end_t = 1150)










if __name__ == "__main__":
    main()

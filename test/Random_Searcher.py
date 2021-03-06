
# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import importlib
import matplotlib.pyplot as plt
import numpy as np
import copy
import statistics
import datetime

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
import Point
importlib.reload(Point)
from Point import Point
import Data_Saver


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
importlib.reload(Data_Saver)




def ExcludeOverTime(max_time, dataRecorder):
    x, y, t, pollutions = dataRecorder.GetAllData()
    new_x = list()
    new_y = list()
    for i in range(len(x)):
        if(t[i] <= max_time):
            new_x.append(x[i])
            new_y.append(y[i])

    return new_x, new_y



def PrintSearchingMoment(fileDir, indexNames, pollutionReshaper, dataRecorder, start_t, end_t, time_step):

    x, y, t, pollution = dataRecorder.GetAllData()
    first_x = x[0]
    first_y = y[0]
    last_x = x[-1]
    last_y = y[-1]


    for t_i in range(start_t, end_t, time_step):
        path = fileDir + str(t_i) + ".pkl"
        draw_x, draw_y, pollutions = pollutionReshaper.Reshape(path, indexNames)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.set_xlabel("x [m]")
        ax.set_ylabel("y [m]")

        ax.scatter(draw_x, draw_y, s= 20,  c = pollutions, cmap = 'binary')
        ax.scatter(first_x, first_y, s= 30,  c = 'red')

    ################################################################
        x, y = ExcludeOverTime(max_time = t_i, dataRecorder = dataRecorder)
        ax.plot(x, y, c = 'blue', linewidth = 1)

        plt.show()
        savePath = "../PollutionCreate/Pic_Pollution/" + str(t_i)  + ".png"

        fig.savefig(savePath, dpi = 300)







def MakePointsFromXY(x, y):
    points = list()
    for i in range(len(x)):
        new_point = Point(x[i], y[i])
        points.append(new_point)

    return points






def DetectFirstReachedPointIndexToOrigin(searhedPoints, originPoint, reachJudgeDistance):
    points = searhedPoints

    for p_i in points:
        distance = p_i.distance(originPoint)
        isReached = (distance <= reachJudgeDistance)
        if(isReached):
            print(isReached)
            ind = points.index(p_i)
            return ind

    return None




def Search(pollutionFileDir, firstDirection, maxStraightLineSearchDistance, search_max_time):
    #???1 ????????????????????????
    coordinateCalculator = Coordinate_Calculator.CoordinateCalculator()

    #???2???????????????????????????
    func = Linear_Function.LinearFunction(maxValue = 100, maxPoint = 0, zeroPoint = 180)
    distCalculator = Linear_Function_Ret_Int.LinearFunctionRetInt(func)
    distMaker = Probability_Distribution_Creater.Degrees_Distribution_Creater(distCalculator)
    chooser = Next_Direction_Chooser.NextDirectionChooser(distMaker)

    #???3 ????????????????????????
    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader(pollutionFileDir, "pkl", pklReader)
    dataRecorder = Data_Recorder.DataRecorder()
    field = Field.FieldClass(dict(uprX = 99, uprY = 99, uprT = 2999, lwrX = 0, lwrY = 0, lwrT = 0))
    onePointSearcher = One_Point_Searcher.OnePointSearcher(dataRecorder, field, pollutionReader)
    lineSearcher = Straight_Line_Searcher.StraightLineSearcher(onePointSearcher)

    #???4????????????????????????
    params = Params.ParamsClass(dict(distElements = np.arange(-180.0, 180.0, 0.1), excludeDegreeWidth = 30))


    # ??????1

    surroundingSearcher = Surrounding_Searcher.SurroundingSearcher(chooser, lineSearcher, coordinateCalculator, params)



    randomMoveSearcher = Random_Move_Searcher.RandomMoveSearcher(lineSearcher)




    randomSearcher = Random_Searcher.RandomSearcher(surroundingSearcher, randomMoveSearcher)
    print(randomSearcher.Search(start_time              = 1000,\
                          max_time                      = 1000 + search_max_time,\
                          start_x                       = 50,\
                          start_y                       = 50,\
                          max_random_x                  = 99,\
                          max_random_y                  = 99,\
                          min_random_x                  = 0,\
                          min_random_y                  = 0,\
                          firstDirection                = firstDirection,\
                          threshold                     = 10,\
                          speed                         = 5,\
                          maxStraightLineSearchDistance = maxStraightLineSearchDistance\
                          ))

    return dataRecorder


def Animation(dataRecorder):

    pklReader = Pickle_Reader.PickleReader()
    fileDir = "/home/kazuma/??????/PollutionCreate/DataLog/2022???/1???/3???/22???/49???/16???/"
    indexNames = Saved_Pollution_Indexs.SavedPollutionIndexs("pollutions", "x", "y")
    pollutionReshaper = Pollution_Data_Reshaper.PollutionDataReshaper(pklReader)

    PrintSearchingMoment(fileDir, indexNames, pollutionReshaper, dataRecorder, start_t = 1000, end_t = 1150, time_step = 10)


def FirstReachedIndex(originPoint, origin2Point, judgeDistance, dataRecorder):
    x, y, t, pollution = dataRecorder.GetAllData()
    points = MakePointsFromXY(x, y)
    ind = DetectFirstReachedPointIndexToOrigin(points, originPoint, judgeDistance)
    if(ind is None):
        ind = DetectFirstReachedPointIndexToOrigin(points, origin2Point, judgeDistance)

    return ind


def IsSuccess(index):
    if(not(index is None)):
        return True

    return False


def CreateDirectoryToDataLog(dirName):

    if(os.path.isdir(dirName)):
        pass
    else:
        os.makedirs(dirName)






def main():

    search_max_time = 150

    pollutionFileDir = "/home/kazuma/??????/PollutionCreate/DataLog/2022???/1???/3???/22???/49???/16???/"

    origin1_x = 0
    origin1_y = 10
    origin2_x = 0
    origin2_y = 80

    saver = Data_Saver.DataSaver()
    saveDir = input("input save directory")
    saveFileAppendix = input("input appendix to save searching file")

    for maxStraightLineSearchDistance in [1, 2, 5, 10, 15, 30, 50]:
        for firstDirection in [0, 60, 120, 180, 210, 240, 300]:
            for search_i in range(10):

                dataRecorder = Search(pollutionFileDir, firstDirection, maxStraightLineSearchDistance, search_max_time)
                #Animation(dataRecorder)

                x, y, t, pollution = dataRecorder.GetAllData()
                indexNames = ['x', 'y', 't', 'pollution', 'search_depth', 'firstDirection', 'origin1_x', 'origin1_y', 'origin2_x', 'origin2_y', 'filePath']
                values = [x, y, t, pollution, maxStraightLineSearchDistance, firstDirection, origin1_x, origin1_y, origin2_x, origin2_y, pollutionFileDir]
                saveDirectoryName = saveDir + "/" + "search_depth_" + str(maxStraightLineSearchDistance) + "_" + "firstDirection" + "_" + str(firstDirection) + "_" + saveFileAppendix
                CreateDirectoryToDataLog(saveDirectoryName)
                savePath = saveDirectoryName + "/" + str(search_i) + '.pkl'
                saver.Save(indexNames, values, savePath)















if __name__ == "__main__":
    main()

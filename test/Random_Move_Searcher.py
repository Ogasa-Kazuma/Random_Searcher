

# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import matplotlib.pyplot as plt

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
import Pollution_Data_Reshaper
import Saved_Pollution_Indexs




importlib.reload(Searching_Data_Recorder)
importlib.reload(Data_Recorder)
importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)
importlib.reload(Field)
importlib.reload(One_Point_Searcher)
importlib.reload(Straight_Line_Searcher)
importlib.reload(Time_Limitter)
importlib.reload(Random_Move_Searcher)
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

    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    dataRecorder = Data_Recorder.DataRecorder()
    field = Field.FieldClass(dict(uprX = 99, uprY = 99, uprT = 2999, lwrX = 0, lwrY = 0, lwrT = 0))
    onePointSearcher = One_Point_Searcher.OnePointSearcher(dataRecorder, field, pollutionReader)

    lineSearcher = Straight_Line_Searcher.StraightLineSearcher(onePointSearcher)
    randomMoveSearcher = Random_Move_Searcher.RandomMoveSearcher(lineSearcher)
    print(randomMoveSearcher.Search(start_x = 50,\
                                    start_y = 50,\
                                    start_time = 10,\
                                    max_time = 200,\
                                    max_x = 99,\
                                    max_y = 99,\
                                    min_x = 0,\
                                    min_y = 0,\
                                    speed = 2,\
                                    threshold = 10))

    print(pollutionReader.Read(56, 63, 30.5))
    print(dataRecorder.GetAllData())


    fileDir = "/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/"
    indexNames = Saved_Pollution_Indexs.SavedPollutionIndexs("pollutions", "x", "y")
    pollutionReshaper = Pollution_Data_Reshaper.PollutionDataReshaper(pklReader)

    PrintSearchingMoment(fileDir, indexNames, pollutionReshaper, dataRecorder, start_t = 10, end_t = 500)








if __name__ == "__main__":
    main()

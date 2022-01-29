

import Animation_Maker
import Pickle_Reader
import Saved_Pollution_Indexs
import importlib

import Pollution_Drawer
import Pollution_Data_Reshaper

import matplotlib.pyplot as plt


import importlib










importlib.reload(Animation_Maker)
importlib.reload(Saved_Pollution_Indexs)
importlib.reload(Pollution_Drawer)
importlib.reload(Pollution_Data_Reshaper)

class SearchingDatas:

    def __init__(self, xList, yList, timeList):
        self.__xList = xList
        self.__yList = yList
        self.__timeList = timeList

    def GetXList(self):
        return self.__xList

    def GetYList(self):
        return self.__yList

    def GetTimeList(self):
        return self.__timeList




pklReader = Pickle_Reader.PickleReader()
searchingResult = pklReader.Read("/home/kazuma/研究/RandomSearcher/ResultLog0126/search_depth_10_firstDirection_240_0126_1715/5.pkl")
print(type(searchingResult['x'].values.tolist()))

xList = searchingResult['x'].values.tolist()
yList = searchingResult['y'].values.tolist()
timeList = searchingResult['t'].values.tolist()
print(searchingResult['filePath'].values.tolist())


searchingDatas = SearchingDatas(xList, yList, timeList)
print(searchingDatas.GetTimeList())

reshaper = Pollution_Data_Reshaper.PollutionDataReshaper(pklReader)
indexNames = Saved_Pollution_Indexs.SavedPollutionIndexs("pollutions", 'x', 'y')

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_aspect('equal')
# ax.set_xlabel("x [m]")
# ax.set_ylabel("y [m]")
drawer = Pollution_Drawer.PollutionDrawer(reshaper)
pollutionFileDir = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒"

#Thesis_Anime_0126/
saveName = input("input save directory and file name")
animeMaker = Animation_Maker.AnimationMaker(drawer)
animeMaker.Make(pollutionFileDir, searchingDatas, show_step = 25, indexNames = indexNames, isSave = True, saveName = saveName)

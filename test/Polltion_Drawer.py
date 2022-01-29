import Pollution_Drawer
import Pickle_Reader
import Pollution_Data_Reshaper
import Saved_Pollution_Indexs

import matplotlib.pyplot as plt

import importlib


importlib.reload(Pollution_Drawer)
importlib.reload(Pickle_Reader)
importlib.reload(Pollution_Data_Reshaper)
importlib.reload(Saved_Pollution_Indexs)


pklReader = Pickle_Reader.PickleReader()
reshaper = Pollution_Data_Reshaper.PollutionDataReshaper(pklReader)
indexNames = Saved_Pollution_Indexs.SavedPollutionIndexs("pollutions", 'x', 'y')

fig = plt.figure()
ax = fig.add_subplot(111)
drawer = Pollution_Drawer.PollutionDrawer(reshaper)
pollutionFile = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/0.pkl"
ax = drawer.Draw(ax, pollutionFile, indexNames)
pollutionFile = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/100.pkl"
ax.set_aspect('equal')
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.scatter(1, 1, c = 'red')
ax.plot([20, 50], [79, 30], c = 'blue')

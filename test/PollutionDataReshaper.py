import importlib
import Pollution_Data_Reshaper
import Pickle_Reader

import matplotlib.pyplot as plt


importlib.reload(Pollution_Data_Reshaper)
importlib.reload(Pickle_Reader)


class PollutionDataParams:
    def __init__(self, pollutionIndex, xIndex, yIndex):

        self.__pollutionIndex = pollutionIndex
        self.__x = xIndex
        self.__y = yIndex

    def Pollution(self):
        return self.__pollutionIndex

    def xlim(self):
        return self.__x

    def ylim(self):
        return self.__y

def main():

    params = PollutionDataParams(pollutionIndex = "pollutions", xIndex = 'x', yIndex = 'y')
    pklReader = Pickle_Reader.PickleReader()
    pollutionReshaper = Pollution_Data_Reshaper.PollutionDataReshaper(pklReader)
    file = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/0.pkl"
    draw_x, draw_y, pollutions = pollutionReshaper.Reshape(file, params)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.scatter(draw_x, draw_y, s= 20,  c = pollutions, cmap = 'binary')




if __name__ == "__main__":
    main()

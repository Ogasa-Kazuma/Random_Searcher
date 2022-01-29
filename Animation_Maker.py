
import matplotlib.pyplot as plt


class AnimationMaker:

    def __init__(self, pollutionDrawer):
        self.__pollutionDrawer = pollutionDrawer


    def Make(self, pollutionFileDir, searchingDatas, show_step, indexNames, isSave = False, saveName = None):


        start_time, last_time = self.__AnimationTimeRange(searchingDatas)
        start_time, last_time = self.__RoundAnimationTime(start_time, last_time)
        end_time = last_time + 1

        for time_i in range(start_time, end_time, show_step):

            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.set_aspect('equal')
            ax.set_xlabel("x [m]")
            ax.set_ylabel("y [m]")

            pollutionFile = pollutionFileDir + "/" + str(time_i) + ".pkl"

            ax = self.__MakePollutionScatter(ax, pollutionFile, indexNames)
            xList, yList = self.__ExcludeOverTime(time_i, searchingDatas)

            ax = self.__DrawSearchedPoints(ax, xList, yList)
            ax = self.__DrawStartPoint(ax, xList, yList)
            if(isSave):
                self.__SavePic(fig, saveName, time_i)
            print(time_i)


        ax = self.__DrawLastPoint(ax, xList, yList)
        if(isSave):
            self.__SavePic(fig, saveName, last_time)

        return ax

    def __AnimationTimeRange(self, searchingDatas):
        t = searchingDatas.GetTimeList()
        start_time = t[0]
        end_time = t[-1]
        return start_time, end_time


    def __RoundAnimationTime(self, start_time, end_time):
        start_time = round(start_time)
        end_time = round(end_time)

        return start_time, end_time

    def __MakePollutionScatter(self, ax, pollutionFile, indexNames):
        ax = self.__pollutionDrawer.Draw(ax, pollutionFile, indexNames)
        return ax

    def __ExcludeOverTime(self, max_time, searchingDatas):
        x = searchingDatas.GetXList()
        y = searchingDatas.GetYList()
        t = searchingDatas.GetTimeList()

        new_x = list()
        new_y = list()
        for i in range(len(x)):
            if(t[i] <= max_time):
                new_x.append(x[i])
                new_y.append(y[i])

        return new_x, new_y



    def __DrawStartPoint(self, ax, xList, yList):
        ax.scatter(xList[0], yList[0], marker = 'D', c = 'darkorange', linewidth = 0.5, ec = 'black', zorder = 2)
        return ax




    def __DrawSearchedPoints(self, ax, xList, yList):

        ax.plot(xList, yList, c = 'dodgerblue', linewidth = 1, zorder = 1)

        return ax


    def __DrawLastPoint(self, ax, xList, yList):
        ax.scatter(xList[-1], yList[-1], marker = 'D', c = 'aqua', linewidth = 0.5, ec = 'black', zorder = 2)
        return ax


    def __SavePic(self, fig, saveName, time):
        fig.savefig(str(saveName) + str(time) + '.png', dpi = 300)

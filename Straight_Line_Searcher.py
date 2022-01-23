
import math

class StraightLineSearcher:


    def __init__(self, pointSearcher):

        self.__pointSearcher = pointSearcher


    def Search(self, kwargs):
        threshold = kwargs['threshold']
        x1 = kwargs['x1']
        x2 = kwargs['x2']
        y1 = kwargs['y1']
        y2 = kwargs['y2']
        start_time = kwargs['start_time']
        max_time = kwargs['max_time']
        speed = kwargs['speed']

        x, y, t, concent = self.__SearchLine(threshold, x1, x2, y1, y2, start_time, max_time, speed)
        return x, y, t, concent



    def __SearchLine(self, threshold, x1, x2, y1, y2, start_time, max_time, speed):
        print("start straight line" + str(start_time))
        x_points, y_points, times = self.__SpecifyPointsBetweenTwoPoints(x1, x2, y1, y2, start_time, speed)

        for point_i in range(len(x_points)):


            try:
                x, y, t, concent = self.__pointSearcher.Search(x_points[point_i], y_points[point_i], times[point_i])
            except ValueError:
                return x, y, t, concent

            if(self.__IsTimeOver(t, max_time)):
                return x, y, t, concent

            if(concent > threshold):
                return x, y, t, concent

        return x, y, t, concent


    def __IsTimeOver(self, time, max_time):
        isTimeOver = (time >= max_time)
        return isTimeOver

    def __LastData(self, x, y, t, pollution):
        last_x = x
        last_y = y
        last_t = t
        last_pollution = pollution
        return last_x, last_y, last_t, last_pollution



    def __SpecifyPointsBetweenTwoPoints(self, x1, x2, y1, y2, begin_time, speed):

        #2点間の角度計算
        angle = math.atan2((y2 - y1), (x2 - x1))
        distance = math.sqrt((x2 - x1) ** (2) + (y2 - y1) ** (2))

        xList, yList = self.__CalcPointsOnLine(distance, angle, x1, y1)
        xList, yList = self.__RoundPoints(xList, yList)



        xList, yList = self.__DeleteDupl(xList, yList)
        xList, yList = self.__ToInt(xList, yList)



        t = self.__TimeList(x1, xList, y1, yList, begin_time, speed)



        return xList, yList, t


    def __CalcPointsOnLine(self, distance, angle, start_x, start_y):

        x = list()
        y = list()

        for i in range(0, round(distance * 10), 1):

            dis_i = i * 0.1
            x.append(start_x + dis_i * math.cos(angle))
            y.append(start_y + dis_i * math.sin(angle))

        return x, y


    def __RoundPoints(self, xList, yList):

        xList = list(map(round, xList))
        yList = list(map(round, yList))

        return xList, yList


    def __DeleteDupl(self, xList, yList):

        new_x = list()
        new_y = list()

        for i in range(len(xList)):
            if(not(xList[i] in new_x and yList[i] in new_y)):
                new_x.append(xList[i])
                new_y.append(yList[i])


        return new_x, new_y


    def __ToInt(self, xList, yList):

        xList = list(map(int, xList))
        yList = list(map(int, yList))



        return xList, yList



    def __TimeList(self, start_x, xList, start_y, yList, begin_time, speed):

        timeList = list()

        for i in range(len(xList)):
            distance = math.sqrt((xList[i] - start_x) ** (2) + (yList[i] - start_y) ** (2))
            t = begin_time + self.__CalcTime(distance, speed)
            timeList.append(t)

        return timeList


    def __CalcTime(self, distance, speed):

        t = distance / speed

        return t

    def __ReturnNotFind(self):
        return 0, 0, 0, 0

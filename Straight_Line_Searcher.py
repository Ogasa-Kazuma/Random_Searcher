
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
        x_points, y_points, times = self.__SpecifyPointsBetweenTwoPoints(x1, x2, y1, y2, start_time, speed)
        x = None
        y = None
        t = None
        concent = None
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

        x, y, t = list(), list(), list()

        #2点を結ぶ直線状の座標を全て計算
        for distance_i in range(0, round(distance)):
            x.append(round(x1 + distance_i * math.cos(angle)))
            y.append(round(y1 + distance_i * math.sin(angle)))
            time = begin_time + self.__CalcTime(distance_i, speed)
            t.append(time)

        return x, y, t

    def __CalcTime(self, distance, speed):

        t = distance / speed

        return t

    def __ReturnNotFind(self):
        return 0, 0, 0, 0

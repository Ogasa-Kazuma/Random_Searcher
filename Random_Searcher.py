
import math
import matplotlib.pyplot as plt

class RandomSearcher:

    def __init__(self, surroundingSearcher, randomMoveSearcher):
        self.__surroundingSearcher = surroundingSearcher
        self.__randomMoveSearcher = randomMoveSearcher

    def Search(self, start_time, max_time, start_x, start_y, max_random_x, max_random_y, min_random_x, min_random_y, firstDirection, threshold, speed, maxStraightLineSearchDistance):


        x, y, direction = self.__DefineFirstMoveState(start_x, start_y, firstDirection)
        t = start_time

        while(1):

            last_x = x
            last_y = y


            print("before surrounding" + str(t))
            x, y, t, pollution = self.__CloseToOrigin(x, y, direction, threshold, t, max_time, speed, maxStraightLineSearchDistance)
            print(x, y, t, pollution)
            if(self.__IsTimeOver(t, max_time)):
                return x, y, t, pollution
            if(pollution > threshold):
                threshold = pollution



            x, y, t, pollution = self.__RandomMove(x, y, max_random_x, max_random_y, min_random_x, min_random_y, t, max_time, speed, threshold)
            if(self.__IsTimeOver(t, max_time)):
                return x, y, t, pollution

            direction = self.__CalcNextDirection(last_x, x, last_y, y)
            if(pollution > threshold):
                threshold = pollution


    def __DefineFirstMoveState(self, start_x, start_y, firstDirection):
        return start_x, start_y, firstDirection


    def __IsTimeOver(self, time, max_time):
        isTimeOver = (time >= max_time)
        return isTimeOver


    def __CloseToOrigin(self, start_x, start_y, baseDirection, threshold, start_time, max_time, speed, maxStraightLineSearchDistance):

        x = start_x
        y = start_y
        t = start_time
        direction = baseDirection

        while(1):
            print("__CloseToOrigin" + str(t))
            x, y, t, pollution = self.__surroundingSearcher.Search(x, y, direction, threshold, t, max_time, speed, maxStraightLineSearchDistance)

            if(self.__IsTimeOver(t, max_time)):
                return x, y, t, pollution

            if(pollution <= threshold):
                return x, y, t, pollution

            if(pollution > threshold):
                threshold = pollution





    def __RandomMove(self, start_x, start_y, max_x, max_y, min_x, min_y, start_time, max_time, speed, threshold):
        while(1):
            print("start t __RandomMove t" + str(start_time))
            x, y, t, pollution = self.__randomMoveSearcher.Search(start_x, start_y, start_time, max_time, max_x, max_y, min_x, min_y,speed, threshold)
            print("__RandomMove t, " + str(t))
            if(self.__IsTimeOver(t, max_time)):
                return x, y, t, pollution
            if(pollution > threshold):
                return x, y, t, pollution

    def __CalcNextDirection(self, x, next_x, y, next_y):
        diff_x = next_x - x
        diff_y = next_y - y

        angle = math.atan2(diff_y, diff_x)

        return angle




    def __ChoiceNextDirection(self):
        self.__directionDecender.Choice()

    def __HasSearchedNear():
        return self.__directionDecender.IsEnd()

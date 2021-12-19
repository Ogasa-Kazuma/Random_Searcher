
import math

class RandomSearcher:

    def __init__(self, timeLimitter, surroundingSearcher, randomMoveSearcher):
        self.__timeLimitter = timeLimitter
        self.__surroundingSearcher = surroundingSearcher
        self.__randomMoveSearcher = randomMoveSearcher

    def Search(self, start_time, start_x, start_y, max_random_x, max_random_y, min_random_x, min_random_y, firstDirection, threshold, speed, maxStraightLineSearchDistance):

        self.__StartTimeCount(start_time)
        x, y, direction = self.__DefineFirstMoveState(start_x, start_y, firstDirection)

        while(1):

            last_x = x
            last_y = y

            x, y, t, pollution = self.__CloseToOrigin(x, y, direction, threshold, speed, maxStraightLineSearchDistance)
            print(x, y, t, pollution)
            if(self.__IsTimeOver()):
                return x, y, t, pollution

            x, y, t, pollution = self.__RandomMove(x, y, max_random_x, max_random_y, min_random_x, min_random_y, speed, threshold)
            if(self.__IsTimeOver()):
                return x, y, t, pollution

            direction = self.__CalcNextDirection(last_x, x, last_y, y)
            if(pollution > threshold):
                threshold = pollution


    def __DefineFirstMoveState(self, start_x, start_y, firstDirection):
        return start_x, start_y, firstDirection


    def __StartTimeCount(self, start_time):
        self.__timeLimitter.Start(start_time)

    def __IsTimeOver(self):
        return self.__timeLimitter.IsTimeOver()


    def __CloseToOrigin(self, start_x, start_y, baseDirection, threshold, speed, maxStraightLineSearchDistance):

        x = start_x
        y = start_y
        direction = baseDirection

        while(1):
            x, y, t, pollution = self.__surroundingSearcher.Search(x, y, direction, threshold, speed, maxStraightLineSearchDistance)

            if(self.__IsTimeOver()):
                return x, y, t, pollution

            if(pollution <= threshold):
                return x, y, t, pollution

            if(pollution > threshold):
                threshold = pollution





    def __RandomMove(self, start_x, start_y, max_x, max_y, min_x, min_y, speed, threshold):
        while(1):
            x, y, t, pollution = self.__randomMoveSearcher.Search(start_x, start_y, max_x, max_y, min_x, min_y, speed, threshold)
            if(self.__IsTimeOver()):
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

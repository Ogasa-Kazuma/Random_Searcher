

import random

class RandomMoveSearcher:

    def __init__(self, lineSearcher):

        self.__lineSearcher = lineSearcher


    def Search(self, start_x, start_y, start_time, max_time, max_x, max_y, min_x, min_y, speed, threshold):

        x = start_x
        y = start_y
        t = start_time

        while(1):
            next_x, next_y = self.__NextPosition(min_x, min_y, max_x, max_y)


            x, y, t, pollution = self.__SearchStraightLine(threshold, x, next_x, y, next_y, t, max_time, speed)

            if(self.__IsTimeOver(t, max_time)):
                return x, y, t, pollution

            if(self.__IsFound(threshold, pollution)):
                return x, y, t, pollution

    def __SearchStraightLine(self, threshold, x, next_x, y, next_y, start_time, max_time, speed):
        kwargs = dict(threshold = threshold, x1 = x, x2 = next_x, y1 = y, y2 = next_y, start_time = start_time, max_time = max_time, speed = speed)
        x, y, t, pollution = self.__lineSearcher.Search(kwargs)
        return x, y, t, pollution

    def __IsTimeOver(self, time, max_time):
        isTimeOver = (time >= max_time)
        return isTimeOver



    def __NextPosition(self, min_x, min_y, max_x, max_y):

        next_x = random.randint(min_x, max_x)
        next_y = random.randint(min_y, max_y)
        return next_x, next_y

    def __IsFound(self, threshold, pollution):
        return pollution > threshold

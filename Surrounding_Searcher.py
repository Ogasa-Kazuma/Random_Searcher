

class SurroundingSearcher:

    def __init__(self, directionDecender, straightLineSearcher, coordinateCalculator, params):
        self.__directionDecender = directionDecender
        self.__straightLineSearcher = straightLineSearcher
        self.__coordinateCalculator = coordinateCalculator
        self.__params = params


    def Search(self, start_x, start_y, baseDirection, threshold, speed, maxDistance, maxTime):

        degreeCollection = self.__DistElements()
        self.__InitDist(degreeCollection)

        x, y = start_x, start_y

        while(1):

            if(self.__HasSearched()):
                return x, y, t, pollution

            direction = self.__ChoiceNextDirection(baseDirection)
            x_next, y_next = self.__CalcNextPosition(start_x, start_y, maxDistance, direction)
            x, y, t, pollution = self.__SearchStraightLine(threshold, x, y, x_next, y_next, speed)


            if(pollution > threshold):
                return x, y, t, pollution


    def __DistElements(self):
        return self.__params.GetDistElements()


    def __InitDist(self, degreeCollection):
        self.__directionDecender.InitDist(degreeCollection)


    def __HasSearched(self):
        return self.__directionDecender.IsEnd()


    def __ChoiceNextDirection(self, baseDirection):
        excludeDegreeWidth = self.__params.GetExcludeDegreeWidth()
        direction = baseDirection + self.__directionDecender.Choice(excludeDegreeWidth)
        return direction

    def __CalcNextPosition(self, x, y, maxDistance, direction):
        x_change, y_change = self.__coordinateCalculator.Calc(maxDistance, direction)
        x = x + x_change
        y = y + y_change
        return x, y

    def __SearchStraightLine(self, threshold, x_now, y_now, x_next, y_next, speed):

        args = dict(threshold = threshold, x1 = x_now, x2 = x_next, y1 = y_now, y2 = y_next, speed = speed)
        x, y, t, pollution = self.__straightLineSearcher.Search(args)
        return x, y, t, pollution

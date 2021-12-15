
class Degrees_Distribution_Creater:

    def __init__(self, itemCountCalculator):
        self.__itemCountCalculator = itemCountCalculator

    def Make(self, degreeRange):

        degrees = self.__CreateDegrees(degreeRange)

        return degrees



    def __CreateDegrees(self, degreeRange):
        degrees = list()
        for deg_i in degreeRange:
            degrees = self.__AddElement(deg_i, degrees)

        return degrees


    def __AddElement(self, deg, degrees):
        num = self.__CalcNumber(deg)
        for j in range(0, num):
            degrees.append(deg)

        return degrees

    def __CalcNumber(self, arg):
        return self.__itemCountCalculator(arg)

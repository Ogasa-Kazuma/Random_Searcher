
class LinearFunction:

    def __init__(self, maxPoint, zeroPoint, adjustRatio):
        self.__zeroPoint = zeroPoint
        self.__maxPoint = maxPoint

    def Calc(self, arg):

        dec = self.__CalcDec(arg)
        #1、じゃなくてmax_valueのほうがいいかも
        probability = 1 - dec

        if(probability <= 0):
            probability = 0

            return probability


    def __CalcDec(self, arg):
        dec_ratio = 1 / (self.__ZeroPoint() / 1)
        diff = self.__MaxPoint() - arg
        dec =  dec_ratio * diff
        dec = abs(dec)

        return dec


    def __MaxPoint(self, value = None):
        if(value is None):
            return self.__maxPoint

        self.__maxPoint = value

    def __ZeroPoint(self, value = None):
        if(value is None):
            return self.__zeroPoint

        self.__zeroPoint = value

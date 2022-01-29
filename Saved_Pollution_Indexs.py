
class SavedPollutionIndexs:

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

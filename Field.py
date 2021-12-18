


class FieldClass:

    def __init__(self, kwargs):
        self.__uprX = kwargs['uprX']
        self.__uprY = kwargs['uprY']
        self.__uprT = kwargs['uprT']

        self.__lwrX = kwargs['lwrX']
        self.__lwrY = kwargs['lwrY']
        self.__lwrT = kwargs['lwrT']


    def GetUpperX(self):
        return self.__uprX

    def GetUpperY(self):
        return self.__uprY

    def GetUpperT(self):
        return self.__uprT


    def GetLowerX(self):
        return self.__lwrX

    def GetLowerY(self):
        return self.__lwrY

    def GetLowerT(self):
        return self.__lwrT

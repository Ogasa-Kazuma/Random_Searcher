


class ParamsClass:

    def __init__(self, kwargs):

        self.__distElements = kwargs['distElements']
        self.__excludeDegreeWidth = kwargs['excludeDegreeWidth']


    def GetDistElements(self):

        return self.__distElements



    def GetExcludeDegreeWidth(self):

        return self.__excludeDegreeWidth



class DataRecorder:

    def __init__(self):
        self.__x = list()
        self.__y = list()
        self.__t = list()
        self.__pollution = list()

    def Append(self, x, y, t, pollution):
        self.__x.append(x)
        self.__y.append(y)
        self.__t.append(t)
        self.__pollution.append(pollution)


    def GetAllData(self):
        return self.__x, self.__y, self.__t, self.__pollution

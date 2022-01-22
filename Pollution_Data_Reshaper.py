import copy

class PollutionDataReshaper:

    def __init__(self, fileReader):
        self.__reader = fileReader
        pass


    def Reshape(self, file, indexs):

        pollutionFile = self.__LoadFile(file)
        pollutions = self.__ReadPollutionsData(pollutionFile, indexs)
        pollutions = self.__NormalizePollutions(pollutions)
        xlim, ylim = self.__ReadIndexLimits(pollutionFile, indexs)


        x, y = self.__CorrectIndexOrder(xlim, ylim)

        return x, y, pollutions


    def __LoadFile(self, file):
        pollutionFile = self.__reader.Read(file)
        return pollutionFile

    def __ReadPollutionsData(self, pollutionFile, indexs):

        pollutionIndex = str(indexs.Pollution())
        pollutions = copy.deepcopy(pollutionFile[pollutionIndex])

        return pollutions



    def __NormalizePollutions(self, pollutions):
        pollutions = pollutions.values.tolist()
        maxPln = max(pollutions)
        for i in range(len(pollutions)):
            pollutions[i] = pollutions[i] / maxPln

        return pollutions

    def __ReadIndexLimits(self, pollutionFile, indexs):
        xIndex = indexs.xlim()
        yIndex = indexs.ylim()

        xlim = pollutionFile[xIndex][0]
        ylim = pollutionFile[yIndex][0]

        return xlim, ylim


    def __CorrectIndexOrder(self, xlim, ylim):
        new_x = list()
        new_y = list()

        xlim = int(xlim)
        ylim = int(ylim)
        
        for x_i in range(0, xlim, 1):
            for y_i in range(0, ylim, 1):

                new_x.append(x_i)
                new_y.append(y_i)

        return new_x, new_y

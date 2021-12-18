
import glob
import pandas as pd

class PollutionReader:

    def __init__(self, dirPath, format):
        self.__dirPath = dirPath
        self.__format = '.' + str(format)

    def SetDir(self, dirPath):
        self.__dirPath = dirPath

    def SetFormat(self, format):
        self.__format = '.' + str(format)

    def Read(self, x, y, t):

        t = int(t)
        fileLocation = self.__dirPath + str(t) + self.__format
        i = glob.glob(fileLocation, recursive=True)

        file = pd.read_pickle(str(i[0]))

        count = file['y'][0] * x + y
        concent = file['pollutions'][count]

        del file

        return concent

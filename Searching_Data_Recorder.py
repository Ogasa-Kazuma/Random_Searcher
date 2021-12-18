

class SearchedPositionsRecorder:
    """探索した場所と、その時間を一時的に記録するクラス"""

    __x = list()
    __y = list()

    def __init__(self):

        self.__x = list()
        self.__y = list()

    def Append(self, kwargs):

        self.__x.append(kwargs['x'])
        self.__y.append(kwargs['y'])

        SearchedPositionsRecorder.__x.append(kwargs['x'])
        SearchedPositionsRecorder.__y.append(kwargs['y'])


    def Clear(self):
        self.__x = list()
        self.__y = list()


    def Get_Searched_Positions(self, all = True):

        if(all):
            return SearchedPositionsRecorder.__x,\
                   SearchedPositionsRecorder.__y

        return self.__x, self.__y

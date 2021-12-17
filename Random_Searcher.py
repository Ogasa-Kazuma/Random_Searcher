

class RandomSearcher:

    def __init__(self, directionDecender, straightLineSearcher, timeCalculator):
        self.__directionDecender = directionDecender
        self.__straightLineSearcher = straightLineSearcher
        self.__timeCalculator = timeCalculator

    def Search(self):



        needRandomMove = self.__HasSearchedNear()
        if(not needRandomMove):
            nextDirection = self.__ChoiceNextDirection()






    def __ChoiceNextDirection(self):
        self.__directionDecender.Choice()

    def __HasSearchedNear():
        return self.__directionDecender.IsEnd()

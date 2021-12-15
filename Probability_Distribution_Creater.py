
class Probability_Distribution_Creater:

    def __init__(self, func):
        self.__func = func

    def Create(self, args, ratio):

        elements = list()

        for item_i in args:
            num = ratio * self.__func(item_i)
            for j in range(0, int(num)):
                elements.append(item_i)

        return elements

#################################################################################
import sys,os
sys.path.append(os.pardir)
import matplotlib.pyplot as plt
import importlib
import numpy as np

from RandomSearcher import Next_Direction_Chooser
importlib.reload(Next_Direction_Chooser)


from RandomSearcher import Linear_Function
importlib.reload(Linear_Function)

from RandomSearcher import Linear_Function_Ret_Int
importlib.reload(Linear_Function_Ret_Int)


from RandomSearcher import Probability_Distribution_Creater
importlib.reload(Probability_Distribution_Creater)
###################################################################################



def InitDist(chooser, degrees):
    chooser.InitDist(degrees)

def Choice(chooser, delDegreeRange):
    value = chooser.Choice(delDegreeRange)
    return value


def Visualize(chooser, degrees, choiceCnt):

    results = list()
    zero = list()
    for i in range(0, choiceCnt):
        InitDist(chooser, degrees)
        results.append(Choice(chooser, delDegreeRange = 30))
        zero.append(0)

    plt.scatter(zero, results, c = 'blue', s = 0.05)


def ExcludeSearchedDegree(chooser, degrees, delDegreeRange):
    InitDist(chooser, degrees)
    print(chooser.Choice(delDegreeRange))
    print(chooser.IsEnd())
    print(chooser.Choice(delDegreeRange))
    print(chooser.Choice(delDegreeRange))










##################################### Main ####################################
def main():

    #進行方向選択者オブジェに角度分布作成者オブジェを注入
    func = Linear_Function.LinearFunction(maxValue = 1000, maxPoint = 0, zeroPoint = 90)
    distCalculator = Linear_Function_Ret_Int.LinearFunctionRetInt(func)
    distMaker = Probability_Distribution_Creater.Degrees_Distribution_Creater(distCalculator)
    chooser = Next_Direction_Chooser.NextDirectionChooser(distMaker)

    # Test
    #Visualize(chooser, np.arange(-180.0, 180.0, 0.1), choiceCnt = 100)
    ExcludeSearchedDegree(chooser, np.arange(-180.0, 180.0, 0.1), delDegreeRange = 90)

##############################################################################

if __name__ == "__main__":
    main()

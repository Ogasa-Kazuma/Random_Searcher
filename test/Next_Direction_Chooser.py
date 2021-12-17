import sys,os
sys.path.append(os.pardir)
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








def main():
    func = Linear_Function.LinearFunction(maxValue = 1000, maxPoint = 0, zeroPoint = 90)
    distCalculator = Linear_Function_Ret_Int.LinearFunctionRetInt(func)
    distMaker = Probability_Distribution_Creater.Degrees_Distribution_Creater(distCalculator)
    chooser = Next_Direction_Chooser.NextDirectionChooser(distMaker)

    chooser.InitDist(degreeRange = np.arange(-180.0, 180.0, 0.1))
    result = chooser.Choice(delDegreeRange = 30)

    print(result)


if __name__ == "__main__":
    main()

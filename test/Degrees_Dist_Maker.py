###############################################################################
import sys,os
sys.path.append(os.pardir)
import importlib
import numpy as np
import matplotlib as plt


from RandomSearcher import Linear_Function
importlib.reload(Linear_Function)

from RandomSearcher import Linear_Function_Ret_Int
importlib.reload(Linear_Function_Ret_Int)


from RandomSearcher import Probability_Distribution_Creater
importlib.reload(Probability_Distribution_Creater)
#########################################################################3

def MakeDist(distMaker):
    degrees = np.arange(-180.0, 180.0, 0.1)
    dist = distMaker.Make(degrees)
    return dist

def PrintDist(dist):
    print(dist)





################################## Main #################################################
def main():
    #角度分布作成オブジェに角度分布計算用オブジェを注入
    func = Linear_Function.LinearFunction(maxValue = 10, maxPoint = 0, zeroPoint = 10)
    distCalculator = Linear_Function_Ret_Int.LinearFunctionRetInt(func)
    distMaker = Probability_Distribution_Creater.Degrees_Distribution_Creater(distCalculator)

    # Test
    dist = MakeDist(distMaker)
    PrintDist(dist)



########################################################################################3



if __name__ == "__main__":
    main()

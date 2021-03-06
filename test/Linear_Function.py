
import sys, os
sys.path.append(os.pardir)

import importlib
import numpy as np
import matplotlib.pyplot as plt

import Linear_Function
import Linear_Function_Ret_Int


importlib.reload(Linear_Function)
importlib.reload(Linear_Function_Ret_Int)


class TestParams:

    def __init__(self, maxValue, maxPoint, zeroPoint):
        self.__maxValue = maxValue
        self.__maxPoint = maxPoint
        self.__zeroPoint = zeroPoint

    def GetMaxValue(self):
        return self.__maxValue

    def GetMaxPoint(self):
        return self.__maxPoint

    def GetZeroPoint(self):
        return self.__zeroPoint


def main():

    params = TestParams(100, 0, 180)

    linearFunc = \
    Linear_Function.LinearFunction(params.GetMaxValue(), params.GetMaxPoint(), params.GetZeroPoint())

    results = list()
    degrees = np.arange(-180.0, 180.0, 0.1)
    for i in degrees:
        results.append(linearFunc.Calc(i))


    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel("基準角度との差分[deg]")
    ax.set_xlabel("確率の高さ[-]")
    ax.scatter(degrees, results, c = 'red')


if __name__ == "__main__":
    main()

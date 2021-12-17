
import sys, os
sys.path.append(os.pardir)

import importlib

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

    params = TestParams(1, 0, 30)

    linearFunc = \
    Linear_Function.LinearFunction(params.GetMaxValue(), params.GetMaxPoint(), params.GetZeroPoint())


    intFunc = Linear_Function_Ret_Int.LinearFunctionRetInt(linearFunc)

    result = intFunc.Calc(14.9999999999999999999)
    print(result)

if __name__ == "__main__":
    main()

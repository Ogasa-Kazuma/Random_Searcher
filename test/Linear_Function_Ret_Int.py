
import sys, os
sys.path.append(os.pardir)

import importlib

import Linear_Function
import Linear_Function_Ret_Int


importlib.reload(Linear_Function)
importlib.reload(Linear_Function_Ret_Int)


def main():

    linearFunc = Linear_Function.LinearFunction(maxValue = 1, maxPoint = 0, zeroPoint = 30)
    intFunc = Linear_Function_Ret_Int.LinearFunctionRetInt(linearFunc)
    result = intFunc.Calc(-14)
    print(result)



if __name__ == "__main__":
    main()

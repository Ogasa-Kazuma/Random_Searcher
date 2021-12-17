
import numpy as np
import matplotlib.pyplot as plt

class LinearFunctionRetInt:

    def __init__(self, linearFunc):

        self.__linearFunc = linearFunc

    def Calc(self, input):
        "xとyの線形関数の値を計算"

        #入力に応じた出力の減少を計算
        output = self.__linearFunc.Calc(input)
        output = round(output)


        return output

import numpy as np
import matplotlib.pyplot as plt

class LinearFunction:

    def __init__(self, maxValue, maxPoint, zeroPoint):

        self.__maxValue = maxValue
        self.__zeroPoint = zeroPoint
        self.__maxPoint = maxPoint

    def Calc(self, x):
        "xとyの線形関数の値を計算"

        #入力に応じた出力の減少を計算
        dec = self.__CalcDec(x)
        y = self.__maxValue - dec

        if(y <= 0):
            y = 0

        return y


    def __CalcDec(self, x):
        "入力に応じた出力の減少を計算"
        #座標と値の減少比
        dec_ratio = self.__DecRatio()
        #最高値を示す座標から離れるほど減少幅が大きくなる
        diff = self.__MaxPoint() - x
        dec =  dec_ratio * diff
        dec = abs(dec)

        return dec


    def __DecRatio(self):
        #線形変化
        r = 1 / (self.__ZeroPoint() / self.__MaxValue())
        return r


    def __MaxPoint(self, value = None):
        if(value is None):
            return self.__maxPoint

        self.__maxPoint = value


    def __ZeroPoint(self, value = None):
        if(value is None):
            return self.__zeroPoint

        self.__zeroPoint = value


    def __MaxValue(self, value = None):
        if(value is None):
            return self.__maxValue

        self.__maxValue = value



def main():

    calculator = LinearFunction(1, 0, 120)
    y = list()
    degrees = np.arange(-180.0, 180.0, 0.1)
    for i in degrees:
        y.append(calculator.Calc(i))

    plt.scatter(degrees, y, c = 'red')

if __name__ == "__main__":
    main()

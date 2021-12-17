
import random

class NextDirectionChooser:

    def __init__(self, degreeDistMaker):
        self.__degreeDistMaker = degreeDistMaker
        self.__degreeDist = None



    def InitDist(self, degreeRange):
        dist = self.__degreeDistMaker.Make(degreeRange)
        self.__Dist(dist)



    def Choice(self, delDegreeRange):

        degree = random.choice(self.__Dist())
        self.__ExcludeSearchedDegree(degree, delDegreeRange)

        return degree


    def IsEnd():
        if(len(self.__Dist()) == 0):
            return True


    def __ExcludeSearchedDegree(self, deg, degRange):

        #0より小さい値は除去
        lwr = self.__DelMinusArea(deg - degRange)
        upr = self.__DelMinusArea(deg + degRange)

        #探索した角度とその周辺の角度は次の探索で使用しない
        narrowed_dist = self.__Exclude(lwr, upr)

        #更新
        self.__Dist(narrowed_dist)

        return None


    def __Exclude(self, lwr, upr):
        "角度確率分布リストから指定範囲の角度を取り除く"
        narrowed_dist = list()
        now_dist = self.__Dist()
        for deg_i in now_dist:
            needExclude = (deg_i >= lwr and deg_i <= upr)
            if(needExclude):
                continue

            narrowed_dist.append(deg_i)

        return narrowed_dist


    def __Dist(self, value = None):
        if(value is None):
            return self.__degreeDist
        self.__degreeDist = value


    def __DelMinusArea(self, number):
        if(number <= 0):
            number = 0

        return number

    def __UpdateDist(self, new_dist):
        self.__Dist(new_dist)

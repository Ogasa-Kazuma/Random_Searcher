
import Pickle_Reader
import matplotlib.pyplot as plt
import Point
import importlib
import statistics

importlib.reload(Point)
from Point import Point
importlib.reload(plt)

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

plt.rcParams['figure.subplot.bottom'] = 0.25
plt.rcParams['figure.subplot.left'] = 0.25

def MakePointsFromXY(x, y):
    points = list()
    for i in range(len(x)):
        new_point = Point(x[i], y[i])
        points.append(new_point)

    return points


def DetectMinDistanceFromEveryOrigins(searchedPoints, originPoints):

    #TODO
    min_distance = searchedPoints[0].distance(originPoints[0])

    for p_i in points:
        for origin_j in originPoints:
            distance = p_i.distance(origin_j)
            if(distance < min_distance):
                min_distance = distance

    return min_distance





def FirstReachedIndex(searchedPoints, originPoints, judgeDistance):

    min_distance = searchedPoints[0].distance(originPoints[0])

    for p_i in searchedPoints:
        for origin_j in originPoints:
            distance = p_i.distance(origin_j)
            if(distance <= judgeDistance):
                return searchedPoints.index(p_i)

    return None


def IsSuccess(index):
    if(not(index is None)):
        return True

    return False



def DiscoverFirstIndexReachedOrigin(fileReader, resultDataDir, sample_count, origins, judgeDistance, start_time):

    searching_time = list()
    success_count = list()

    for sample_i in range(sample_count):
        searchingResult = fileReader.Read(resultDataDir + str(sample_i) + ".pkl")
        xList = searchingResult['x'].values.tolist()
        yList = searchingResult['y'].values.tolist()
        timeList = searchingResult['t'].values.tolist()
        pollutionList = searchingResult['pollution'].values.tolist()

        searchedPoints = MakePointsFromXY(xList, yList)
        index = FirstReachedIndex(searchedPoints, origins, judgeDistance)

        if(index is None):
            print(timeList[-1] - start_time)
            searching_time.append(timeList[-1] - start_time)
            success_count.append(0)
        else:
            print(timeList[index] - start_time)
            searching_time.append(timeList[index] - start_time)
            success_count.append(1)


    return searching_time, success_count








searching_time_mean_list = list()
success_count_mean_list = list()


def main():

    origin1 = Point(0, 10)
    origin2 = Point(0, 80)
    origins = [origin1, origin2]

    pklReader = Pickle_Reader.PickleReader()
    search_depth = [1, 2, 5, 10, 15, 30, 50]
    search_direction = [0, 60, 120, 180, 210, 240, 300]




    for search_i in search_direction:



        resultDataDir = "/home/kazuma/研究/RandomSearcher/ResultLog0126/search_depth_" + str(10) + "_firstDirection_" + str(search_i) + "_" + "0126_1715" + "/"
        print("")
        print(str(search_i))
        searching_time, success_count = DiscoverFirstIndexReachedOrigin(pklReader, resultDataDir, sample_count = 10, origins = origins, judgeDistance = 10, start_time = 1000)

        print("mean and sd")
        print(statistics.mean(searching_time))
        print(statistics.pstdev(searching_time))

        print(statistics.mean(success_count))
        print(statistics.pstdev(success_count))

        searching_time_mean_list.append(statistics.mean(searching_time))
        success_count_mean_list.append(statistics.mean(success_count))

        #plt.scatter(search_depth, statistics.mean(searching_time), c = 'navy')
    fig = plt.figure()
    fig2 = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig2.add_subplot(111)


    ax1.set_xlabel("移動基準角度 [deg]", fontsize = 12, labelpad = 18)
    ax1.set_ylabel("探索時間 [s]", fontsize = 12, labelpad = 18)

    ax1.plot(search_direction, searching_time_mean_list, c= 'blue')

    ax2.set_xlabel("移動基準角度 [deg]", fontsize = 12, labelpad = 18)
    ax2.set_ylabel("探索成功率 [-]", fontsize = 12, labelpad = 18)

    ax2.plot(search_direction, success_count_mean_list, c= 'red')

    fig.savefig("Thesis_Data/" + str(input()) + '.png', dpi = 300)
    fig2.savefig("Thesis_Data/" + str(input()) + '.png', dpi = 300)



if __name__ == "__main__":
    main()

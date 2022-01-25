
import Pickle_Reader
import matplotlib.pyplot as plt
import Point
import importlib
import statistics

importlib.reload(Point)
from Point import Point





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

    for sample_i in range(sample_count):
        searchingResult = fileReader.Read(resultDataDir + str(sample_i) + ".pkl")
        xList = searchingResult['x'].values.tolist()
        yList = searchingResult['y'].values.tolist()
        timeList = searchingResult['t'].values.tolist()
        pollutionList = searchingResult['pollution'].values.tolist()

        searchedPoints = MakePointsFromXY(xList, yList)
        index = FirstReachedIndex(searchedPoints, origins, judgeDistance)

        if(index is None):
            searching_time.append(timeList[-1] - start_time)
            success_count.append(0)
        else:
            searching_time.append(timeList[index] - start_time)
            success_count.append(1)








searching_time = list()
success_count = list()


def main():

    origin1 = Point(0, 10)
    origin2 = Point(0, 80)
    origins = [origin1, origin2]

    pklReader = Pickle_Reader.PickleReader()
    resultDataDir = "/home/kazuma/研究/RandomSearcher/SearchingDataLog/search_depth_15_firstDirection_215/"

    DiscoverFirstIndexReachedOrigin(pklReader, resultDataDir, sample_count = 3, origins = origins, judgeDistance = 5, start_time = 1000)

    print(statistics.mean(searching_time))
    print(statistics.pstdev(searching_time))

    print(statistics.mean(success_count))
    print(statistics.pstdev(success_count))


if __name__ == "__main__":
    main()

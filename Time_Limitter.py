

class TimeLimitter:


    def __init__(self, limitFromStart_s):
        self.__start_time = None
        self.__limitTimeLength = limitFromStart_s
        self.__latestTime = None

        self.__isInitialized = False
        self.__isFinished = False
        self.__isOver = False

    def Start(self, start_time):
        if(self.__isInitialized):
            raise ValueError('時間制限オブジェクトのStartメソッドの呼び出しは1回だけでお願いします')
        self.__start_time = start_time
        self.__latestTime = start_time
        self.__isInitialized = True

    def Update(self, time):
        if(time < self.__latestTime):
            raise ValueError('人は過去には戻れない（光月トキ)')
        self.__latestTime = time


    def IsTimeOver(self):
        if(self.__latestTime - self.__start_time > self.__limitTimeLength):
            self.__isOver = True

        return self.__isOver

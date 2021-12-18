# -*- coding: utf-8 -*-
# test_sample.py
from unittest import TestCase
import sys, os
sys.path.append(os.pardir)


import importlib

import Searching_Data_Recorder
import Pollution_Reader
import Pickle_Reader

importlib.reload(Searching_Data_Recorder)
importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)


def main():
    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    dataRecorder = Searching_Data_Recorder.SearchingDataRecorder(pollutionReader)

    dataRecorder.Append(dict(x = 90, y = 90, speed = 2))
    print(dataRecorder.GetAllData())
    dataRecorder.Append(dict(x = 99, y = 99, speed = 2))
    print(dataRecorder.GetAllData())
    dataRecorder.Append(dict(x = 30, y = 60, speed = 2))
    print(dataRecorder.GetAllData())

if __name__ == "__main__":
    main()

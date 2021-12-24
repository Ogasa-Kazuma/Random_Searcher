


# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.pardir)


import importlib
import Data_Recorder


importlib.reload(Data_Recorder)


def main():

    dataRecorder = Data_Recorder.DataRecorder()
    dataRecorder.Append(1, 2, 3, 4)
    dataRecorder.Append(1, 2, 3, 4)
    print(dataRecorder.GetAllData())

if __name__ == "__main__":
    main()

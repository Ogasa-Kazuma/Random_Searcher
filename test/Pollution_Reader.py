
import sys, os
sys.path.append(os.pardir)

import importlib

import Pollution_Reader
import Pickle_Reader


importlib.reload(Pollution_Reader)
importlib.reload(Pickle_Reader)



def main():


    pklReader = Pickle_Reader.PickleReader()
    pollutionReader = Pollution_Reader.PollutionReader("/home/kazuma/研究/RandomSearcher/DataLog/2021年/12月/3日/18時/40分/6秒/", "pkl", pklReader)
    print(pollutionReader.Read(x = 99, y = 99, t = 90))

if __name__ == "__main__":
    main()

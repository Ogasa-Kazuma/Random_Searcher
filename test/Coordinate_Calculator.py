
import sys, os
sys.path.append(os.pardir)

import importlib

from RandomSearcher import Coordinate_Calculator
importlib.reload(Coordinate_Calculator)





def main():

    coordinateCalculator = Coordinate_Calculator.CoordinateCalculator()
    print(coordinateCalculator.Calc(5, -720))

if __name__ == "__main__":
    main()

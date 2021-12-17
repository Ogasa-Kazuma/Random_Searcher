
import math

class CoordinateCalculator:

    def __init__(self):
        pass

    def Calc(self, radius, theta):
        x = radius * math.cos(math.radians(theta))
        y = radius * math.sin(math.radians(theta))

        return x, y


class PollutionDrawer:

    def __init__(self, pollutionDataReshaper):
        self.__pollutionDataReshaper = pollutionDataReshaper

    def Draw(self, draw_area, pollutionFile, savedIndexNames, draw_size = 20, cmap = 'binary'):
        draw_x, draw_y, pollutions = self.__pollutionDataReshaper.Reshape(pollutionFile, savedIndexNames)

        draw_area.scatter(draw_x, draw_y, s = draw_size,  c = pollutions, cmap = cmap)
        return draw_area

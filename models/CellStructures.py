import math


class CellStructures:
    def __init__(self, totalArea, totalTrafficChannels, radiusOfCell, frequencyReuseFactor):
        self.totalArea = totalArea
        self.totalTrafficChannels = totalTrafficChannels
        # self.cellType = cellType
        self.radiusOfCell = radiusOfCell
        self.frequencyReuseFactor = frequencyReuseFactor
        self.numberOfCells = self.get_numberOfCells()
        self.numberOfChannelsPerCell = self.getNumberOfChannelsPerCell()
        self.totalCapacity = self.getTotalCapacity()
        self.totalNumberOfPossibleConcurrentCall = self.getTotalNumberOfConcurrentCall()

    def get_numberOfCells(self):
        areaOfEachCell = float(2.6*self.radiusOfCell*self.radiusOfCell)
        return round(self.totalArea/areaOfEachCell)

    def getNumberOfChannelsPerCell(self):
        return round(self.totalTrafficChannels/self.frequencyReuseFactor)

    def getTotalCapacity(self):
        return self.numberOfCells * self.numberOfChannelsPerCell

    def getTotalNumberOfConcurrentCall(self):
        return self.totalCapacity

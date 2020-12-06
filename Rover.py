class Rover:
    def __init__(self,startingPoint,direction):
        self.startingPoint = startingPoint
        self.direction = direction

    def showInformation(self):
        return  {"x": self.startingPoint.x, "y": self.startingPoint.y, "direction": self.direction.rawDirection}
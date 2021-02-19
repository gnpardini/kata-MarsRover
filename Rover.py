class Rover:
    def __init__(self, startingPoint, direction):
        self.position = startingPoint
        self.direction = direction

    def showInformation(self):
        return {
            "x": self.position.getX(),
            "y": self.position.getY(),
            "direction": self.direction.asString()
        }

    def moveForward(self):
        
        self.direction.moveForward(self.position)

        
    def moveBackward(self):

        self.direction.moveBackward(self.position)

       
        




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
        direction = self.direction.asString()

        if direction == "N":
            self.position.increaseY() 

        elif direction == "S":
            self.position.decreaseY()

        elif direction == "E":
            self.position.increaseX()
        
        else:
            self.position.decreaseX()
        




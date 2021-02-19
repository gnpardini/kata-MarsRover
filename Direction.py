class Direction:
    def __init__(self,rawDirection):
        self.rawDirection = rawDirection

    def asString(self):
        return self.rawDirection

    def moveForward(self,position):
        if self.rawDirection == "N":
            position.increaseY()
        
        elif self.rawDirection == "S":
            position.decreaseY()
        
        elif self.rawDirection == "E":
            position.increaseX()

        else:
            position.decreaseX()

    def moveBackward(self,position):
        if self.rawDirection == "N":
            position.decreaseY()
        else:
            position.increaseY()
    
class Coordinates:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y 

    def increaseY(self):

        self.y += 1

    def decreaseY(self):

        self.y -= 1

    def increaseX(self):

        self.x += 1

    def decreaseX(self):
        self.x -= 1
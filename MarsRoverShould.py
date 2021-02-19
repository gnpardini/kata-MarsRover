import unittest
from Coordinates import Coordinates
from Direction import Direction
from Rover import Rover

def createRover(stringDirection = "N"):
    x = 12
    y = 5
    startingPoint = Coordinates(x,y)
    direction = Direction(stringDirection)

    return Rover(startingPoint,direction)

class MarsRoverShould(unittest.TestCase):

    def test_showDirectionsAndCoordinates(self):
        rover = createRover()

        information = rover.showInformation()

        self.assertEqual(information, {"x":12, "y": 5, "direction": "N"})
       


    def test_increaseYWhenGoesToNorth(self):
        rover = createRover()

        rover.moveForward()
        information = rover.showInformation()

        self.assertEqual(information, {"x":12, "y": 6, "direction": "N"})


    def test_decreaseYWhenGoesToSouth(self):
        rover = createRover("S")

        rover.moveForward()
        information = rover.showInformation()

        self.assertEqual(information, {"x":12, "y": 4, "direction": "S"})

    def test_increaseXWhenGoesToEast(self):
        rover = createRover("E")

        rover.moveForward()
        information = rover.showInformation()

        self.assertEqual(information, {"x":13, "y": 5, "direction": "E"})


    def test_decreaseXWhenGoesToWest(self):
        rover = createRover("W")

        rover.moveForward()
        information = rover.showInformation()

        self.assertEqual(information, {"x":11, "y": 5, "direction": "W"})

    def test_decreaseYWhenGoesBackwardsFacingNorth(self):
        rover = createRover("N")

        rover.moveBackward()
        information = rover.showInformation()

        self.assertEqual(information, {"x":12, "y": 4, "direction": "N"})

    def test_IncreaseYWhenGoesBackwardsFacingSouth(self):
        rover = createRover("S")

        rover.moveBackward()
        information = rover.showInformation()

        self.assertEqual(information, {"x":12, "y": 6, "direction": "S"})
        
        

if __name__ == '__main__':
    unittest.main()
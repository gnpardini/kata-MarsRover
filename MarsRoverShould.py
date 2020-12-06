import unittest
from Coordinates import Coordinates
from Direction import Direction
from Rover import Rover

class MarsRoverShould(unittest.TestCase):

    def test_upper(self):
        x = 12
        y = 5
        startingPoint = Coordinates(x,y)
        direction = Direction("N")
        rover = Rover(startingPoint,direction)

        information = rover.showInformation()

        self.assertEqual(information, {"x":12, "y": 5, "direction": "N"})
       
        

if __name__ == '__main__':
    unittest.main()
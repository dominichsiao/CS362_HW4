import unittest
import cube

class testCaseCube(unittest.TestCase):
    #test code for normal values
    def test_cube(self):
        self.assertEqual(cube.cube(5), 125)

    #test code for a zero value
    def test_cube_1(self):
        self.assertEqual(cube.cube(0), 0)

    #test code for a negative value
    def test_cube_2(self):
        self.assertEqual(cube.cube(-1), 1)

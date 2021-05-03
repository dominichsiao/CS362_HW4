import unittest
import element

class testCaseCube(unittest.TestCase):
    #test code for normal values
    def test_cube(self):
        self.assertEqual(element.fill_list(5,5,5,5), 25)

    #test code for a zero value
    def test_cube_1(self):
        self.assertEqual(element.fill_list(5,1,4,5), 15)

    #test code for a negative value
    def test_cube_2(self):
        self.assertEqual(element.fill_list(7,-1,3,5), 16)
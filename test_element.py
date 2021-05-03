import unittest
import element

class testCaseElement(unittest.TestCase):
    #test code for normal values
    def test_element(self):
        self.assertEqual(element.fill_list(5,5,5,5), 5)

    #test code for a zero value
    def test_element_1(self):
        self.assertEqual(element.fill_list(5,0,4,5), 3.5)

    #test code for a negative value
    def test_element_2(self):
        self.assertEqual(element.fill_list(7,-1,3,5), 5.33)

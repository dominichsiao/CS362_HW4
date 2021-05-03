import unittest
import name

class testCaseCube(unittest.TestCase):
    #test code for normal values
    def test_name(self):
        self.assertEqual(name.name("Sree", "Gajula"), "Sree Gajula")

    #test if there is no space in between name
    def test_name_1(self):
        self.assertEqual(name.name("Sree", "Gajula"), "SreeGajula")

    #test if first and last names have been switched
    def test_name_2(self):
        self.assertEqual(name.name("Sree", "Gajula"), "Gajula Sree")
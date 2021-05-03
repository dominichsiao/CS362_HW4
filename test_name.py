import unittest
import name

class testCaseName(unittest.TestCase):
	#test for pass case
	def test_name(self):
		self.assertEqual(name.name("Sree", "Gajula"), "Sree Gajula")
	
	#test for no space between names
	def test_name_1(self):
		self.assertEqual(name.name("Sree", "Gajula"), "SreeGajula")

	#test case for first and last name swapped
	def test_name_2(self):
		self.assertEqual(name.name("Sree", "Gajula"), "Gajula Sree")

import unittest
import basic

class Testing(unittest.TestCase):

	def test_unisum(self):
		self.assertEqual(uniquesum(10,5,5), 15)

	def test_che(self):
		self.assertEqual(test(10),10)

if __name__ == '__main__':
    unittest.main()
import unittest
import Library

class TestLibraryMethods(unittest.TestCase):

	def test_insertitem(self, libraryInstance):
		libraryInstance.stock.append(Book(15, "test-title", True, "mrtesty", "Hardback", 2004))

		for s in libraryInstance.stock:
			if(s.idnum == 15):
				self.assertEqual(s.title, "test-title")
				self.assertEqual(s.status, True)
				self.assertEqual(s.author, "mrtesty")
				self.assertEqual(s.btype, "Hardback")
				self.assertEqual(s.year, 2004)


	def test_insertperson(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

libraryInstance = library.Library()

if __name__ == '__main__':
	unittest.main()

		def test_SaveNewspapers(self):
		testPaper1 = Newspaper(2, 1, 1, 1, "The Guardian", False, "09/08/2017")
		testPaper2 = Newspaper(5, 1, 1, 5, "The Sun", True, "10/08/2017")
		listOfPapers = [testPaper1, testPaper2]
		successfull = SaveNewspapers(listOfPapers)
		self.assertEqual(successfull, "Success")
	def test_LoadNewspapers(self):
		listOfPapers = LoadNewspapers()
		self.assertEqual(listOfPapers[0].id, 1)
	def test_SaveBooks(self):
		testBook1 = Book(1, 10, 8, "9781621151593", "Mogworld", "Yahtzee Croshaw", "Dark Horse Books", "23/10/2009", "Fantasy")
		testBook2 = Book(6, 10, 10, "1783522577", "Terrible Old Games You've Probably Never Heard Of", "Stuart Ashens", "Unbound Digital", "03/12/2015", "Non-Fiction")
		listOfBooks = [testBook1, testBook2]
		successfull = SaveBooks(listOfBooks)
		self.assertEqual(successfull, "Success")
	def test_LoadBooks(self):
		listOfBooks = LoadBooks()
		self.assertEqual(listOfBooks[0].isbn, "9781621151593")
if __name__ == '__main__':
	unittest.main()
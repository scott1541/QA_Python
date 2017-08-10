from pprint import pprint

#Library

class Item:

	def __init__(self, idnum, name, status):
		self.idnum = idnum
		self.name = name
		self.status = status

class Book(Item):
	def __init__(self, idnum, name, status, author, btype, year):

		Item.__init__(self, idnum, name, status)
		self.author = author
		self.btype = btype
		self.year = year

class Map(Item):
	def __init__(self, idnum, name, status, scale, publisher, year):

		Item.__init__(self, idnum, name, status)
		self.scale = scale
		self.publisher = publisher
		self.year = year

class Journal(Item):
	def __init__(self, idnum, name, status, edition, publisher, year):

		Item.__init__(self, idnum, name, status)
		self.edition = edition
		self.publisher = publisher
		self.year = year

class Newspaper(Item):
	def __init__(self, idnum, name, status, date):

		Item.__init__(self, idnum, name, status)
		self.date = date

class Person:
	def __init__(self, pidnum, role, name, age, sex, address, email, tel):
		self.pidnum = pidnum
		self.role = role
		self.name = name
		self.age = age
		self.sex = sex
		self.address = address
		self.email = email
		self.tel = tel


class Library:
	stock = [Book(0, "Peter Rabbit", False, "Beatrix Potter", "Hardback", 1950),
			Book(1, "50 Shades of Dev", False, "Ladon Jackson", "Paperback", 2017),
			Map(2, "LandRanger 125", False, "1:50,000", "OS", 2016),
			Journal(3, "British Medical Journal", True, 23, "BMA", 2004),
			Newspaper(4, "Manchester Evening news", False, "25/07/2017")]

	people = [Person(0, "Customer", "Mike Freeman", 32, "m", "34 Fake Street", "mike12@gmail.com", "07451936187"),
			 Person(1, "Customer", "Tom Martin", 21, "m", "3 The Rise", "tommo@hotmail.com", "0723936563"),
			 Person(2, "Customer", "Gary Oldman", 40, "m", "742 Evergreen Terrace", "hs@gmail.com", "04551978297")]

	def openLibrary():

		print("\n Library System (TM) \n")
		print("--------------------------------------------------------")
		print("|  0. List Stock       |   6. List Customers           |")
		print("|  1. Check Out Item   |   7. Register new Person      |")
		print("|  2. Check In Item    |   8. Update Person            |")
		print("|  3. Add new Item     |   9. Remove Person            |")
		print("|  4. Remove Item      |   10. Output Library to File  |")
		print("|  5. Update Item      |   Any other key to exit       |")
		print("--------------------------------------------------------")

		uinput = input("Select: ")

		if(uinput == "0"):
			Library.listStock()
		elif(uinput == "1"):
			Library.checkOut()
		elif(uinput == "2"):
			Library.checkIn()
		elif(uinput == "3"):
			Library.addItem()
		elif(uinput == "4"):
			Library.remItem()
		elif(uinput == "5"):
			Library.updItem()
		elif(uinput == "6"):
			Library.listPer()
		elif(uinput == "7"):
			Library.regPer()
		elif(uinput == "8"):
			Library.updPer()
		elif(uinput == "9"):
			Library.remPer()
		elif(uinput == "10"):
			Library.outFile()
		else:
			quit()


	def listStock():

		for s in Library.stock:
			print(type(s))
			pprint(s.__dict__)

		Library.openLibrary()

	def checkOut():
		checkout = input("Enter ID to check out:")

		for s in Library.stock:
			if(s.idnum == int(checkout)):
				s.status = True
				break

		Library.openLibrary()

	def checkIn():
		checkin = input("Enter ID to check in:")

		for s in Library.stock:
			if(s.idnum == int(checkin)):
				s.status = False
				break
		Library.openLibrary()

	def addItem():
		print("Items")
		print("1. Book")
		print("2. Map")
		print("3. Journal")
		print("4. Newspaper")
		inptype = input("Item to add:")

		if(inptype == "1"):

			print("Add Book")
			title = input("Title:")
			author = input("Author:")
			btype = input("Book Type:")
			year = input("Year:")

			Library.stock.append(Book(len(Library.stock), title, False, author, btype, year))

		elif(inptype == "2"):

			print("Add Map")
			name = input("Name:")
			scale = input("Scale:")
			publish = input("Publisher:")
			year = input("Year:")

			Library.stock.append(Map(len(Library.stock), name, False, scale, publish, year))
		
		elif(inptype == "3"):

			print("Add Journal")
			name = input("Name:")
			edition = input("Edition:")
			publish = input("Publisher:")
			year = input("Year:")

			Library.stock.append(Journal(len(Library.stock), name, False, edition, publish, year))

		elif(inptype == "4"):

			print("Add Newspaper")
			name = input("Name:")
			date = input("Date:")

			Library.stock.append(Journal(len(Library.stock), name, False, date))

		else:
			pass

		Library.openLibrary()

	def remItem():
		remove = input("Enter ID to remove:")

		for s in Library.stock:
			if(s.idnum == int(remove)):
				Library.stock.remove(s)
				break

		Library.openLibrary()

	def updItem():
		update = input("Enter ID to update:")

		for s in Library.stock:
			if(s.idnum == int(update)):

				if(isinstance(s, Book)):
					s.title = input("Title:")
					s.author = input("Author:")
					s.btype = input("Book Type:")
					s.year = input("Year:")

				if(isinstance(s, Map)):
					s.name = input("Name:")
					s.scale = input("Scale:")
					s.publish = input("Publisher:")
					s.year = input("Year:")

				if(isinstance(s, Journal)):
					s.name = input("Name:")
					s.edition = input("Edition:")
					s.publish = input("Publisher:")
					s.year = input("Year:")

				if(isinstance(s, Newspaper)):
					s.name = input("Name:")
					s.date = input("Date:")

				break

		Library.openLibrary()

	def listPer():
		for p in Library.people:
			print("Person :", p.pidnum, p.role, p.name)
			print("\t", p.age, p.sex, p.address, p.email, p.tel)

		Library.openLibrary()

	def regPer():
		print("Add Person:")
		role = input("Role:")
		name = input("Name:")
		age = input("Age:")
		sex = input("Sex:")
		address = input("Address:")
		email = input("Email address:")
		tel = input("Telephone")

		Library.people.append(Person(len(Library.people), role, name, age, sex, address, email, tel))

		Library.openLibrary()

	def remPer():
		remove = input("Enter Person (Name) to remove:")

		for s in Library.people:
			if(s.name == remove):  #Search by name only, ID throws error alongside name
				Library.people.remove(s)
			break

		Library.openLibrary()

	def updPer():
		update = input("Enter Person (Name) to update:")

		for s in Library.people:
			if(s.name == update): 
				print("Update ", s.name)
				s.role = input("Role:")
				s.name = input("Name:")
				s.age = input("Age:")
				s.sex = input("Sex:")
				s.address = input("Address:")
				s.email = input("Email address:")
				s.tel = input("Telephone")
			break

		Library.openLibrary()

	def outFile():
		outPFile = open("library_output.txt", "w+")

		for s in Library.stock:
			outType = (type(s))
			outPFile.write(str(outType))
			outPFile.write("\n")

			if(isinstance(s, Book)):
				out = s.idnum, s.name, s.status, s.author, s.btype, s.year

			if(isinstance(s, Map)):
				out = s.idnum, s.name, s.status, s.scale, s.publisher, s.year

			if(isinstance(s, Journal)):
				out = s.idnum, s.name, s.status, s.edition, s.publisher, s.year

			if(isinstance(s, Newspaper)):
				out = s.idnum, s.name, s.status, s.date

			outPFile.write(str(out))
			outPFile.write("\n")
		
		outPFile.close()

		Library.openLibrary()

Library.openLibrary()
import math
import unittest
import numpy as np

list = []

for i in range(0, 10):
	list.append(i+1)
	print(i+1)

print(list)

#Blackjack
def test(che):
	return che

class Basic():
	def __init__(self):
		pass

	def blackjack(input1, input2):
		if(input1 > 21 and input2 > 21):
			print(0); return 0
		elif(input1 > 21):
			print(input2); return input2
		elif(input2 > 21):
			print(input1); return input1
		elif(input1 > input2):
			print(input1); return input1
		elif(input2 > input1):
			print(input2); return input2
		else:
			print(0); return 0


	def uniquesum(input1, input2, input3):
		usum = 0
		inList = [input1, input2, input3]
		uset = set(inList)
		usum = sum(uset)
		print(usum)

		return usum;

	def toohot(temp, isSummer): 
		if(isSummer):
			if(temp >= 60 and temp <= 100):
				return True
			else:
				return False
		else:
			if(temp >= 60 and temp <= 90):
				return True
			else:
				return False

	def leapyear(year):
		if(year % 4 == 0):
			if(year %400 == 0 or year % 100 != 0):
				return True
			else:
				return False
		else:
			return False

Basic.blackjack(21, 21)

Basic.uniquesum(17,432,3)

Basic.toohot(60, True)

print(Basic.toohot(100, True))

print(Basic.leapyear(2004))


class Interm():
	def __init__(self):
		pass

	def paintwizard(height, width):
		area = height * width

		paints = {'CheapoMax': [20, 10, 19.99, 0, 0, 0, 0],
				'AverageJoes': [15, 11, 17.99, 0, 0, 0, 0],
				'Duluxorious': [10, 20, 25.00, 0, 0, 0, 0]}


		for k in paints:
			paints[k][3] = area / paints[k][1] #litres required
			paints[k][4] = math.ceil(paints[k][3] / paints[k][0]) #tins required
			paints[k][5] = paints[k][4] * paints[k][2] #Total cost
			paints[k][6] = paints[k][4] * paints[k][0] - area / paints[k][1] #Wastage

		names = ["CheapoMax", "AverageJoes", "Duluxorious"]

		costs = [paints['CheapoMax'][5], paints['AverageJoes'][5], paints['Duluxorious'][5]]

		waste = [paints['CheapoMax'][6], paints['AverageJoes'][6], paints['Duluxorious'][6]]

		print("Cheapest Paint: ", names[np.argmin(costs)], "at £", paints[names[np.argmin(costs)]][5])

		print("Least wastage: ", names[np.argmin(waste)], "at", paints[names[np.argmin(waste)]][6], " L")


	def filewrite(intput)

Interm.paintwizard(100,2.5)

class person:

	def __init__(self, name, occup, age)
		self.name = name
		self.occup = occup
		self.age = age



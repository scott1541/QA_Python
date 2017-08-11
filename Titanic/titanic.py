import pandas as pd
import csv
import re
#Titanic

class ImportData:

	sourceList = []

	def read():
		sourceFile = open("titanic.csv")
		reader = csv.DictReader(sourceFile)

		for row in reader:
			ImportData.sourceList.append((row['Name'], row['Sex'], row['Age'], row['Survived'], row['Pclass'], row['Cabin'], row['Ticket'], row['Fare']))

		sourceFile.close()

	def missingData():
		missingA = 0
		totalAge = 0
		missingC = 0

		for row in ImportData.sourceList[1:]:
			if(row[2] != ""):
				totalAge += float(row[2])


		for row in ImportData.sourceList:
			if(row[2] == ""):
				row[2] == totalAge / 714
				missingA += 1

			if(row[5] == ""):
				row[5] == "Unknown"
				missingC += 1


		print("Missing Data")
		print("Age: ", missingA)
		print("Cabin: ", missingC)

	def splitName():
		for row in ImportData.sourceList[1:]:
			new = re.split(',|.', row[0])
			#ImportData.sourceList.insert(new[0],1)
			#ImportData.sourceList.insert(new[3],1)
			#ImportData.sourceList.insert(new[2],1)
			print(new[0])#, new[1])#, new[2], new[1])




ImportData.read()
ImportData.missingData()
ImportData.splitName()

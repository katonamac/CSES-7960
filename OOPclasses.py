#This is where I practice with classes and catch up

import math

math.sqrt(25)

#Think about the functions in the "math" module as being part of a class

class Soil(object):
	'''This is my soil class used to monitor important properties related to the soil health.
	'''
	def __init__(self, basicType, P, K):
		self.basicType = basicType
		self.P = P
		self.K = K

#We add these functions to avoid accessing the instance variables directly	
	def getPvalue(self):
		return self.P

	def getKvalue(self):
		return self.K

	def fertilize(self, Pfert, Kfert, amount):
		'''Increase the predicted amount of P and K in the soil based on the fertilizer applied.
		PFERT: float, percentage of P in fertilizer
		KFERT: float, percentage of K in fertilizer
		AMOUNT: float, lbs of fertilizer per acre
		'''
		self.P = int(self.getPvalue()) + int(Pfert * amount)
		self.K = int(self.getKvalue()) + int(Kfert * amount)

	def checkMinimum(self):
		'''Determine if soil is at minimum level for crop growth.  
		Minimum P: 120
		Mimimum K: 80
		'''
		if self.getPvalue() >= 120:
			print "P levels are adequate.  Current level: " + str(self.getPvalue())
		else:
			print "P levels are low.  Current level: " + str(self.getPvalue())

		if self.getKvalue() >= 80:
			print "K levels are adequate.  Current level: " + str(self.getKvalue())
		else:
			print "K levels are low.  Current level: " + str(self.getKvalue())

	def monthlyLoss(self, rainPerMo):
		'''Calculate the monthly loss based on rainfall.  Assume a 2 point loss for every inch of rain for K and a 0.25 point loss for every inch of rain for 
		'''
		self.K = int(self.getKvalue()) - int(2 * rainPerMo)
		self.P = int(self.getPvalue()) - int(0.25 * rainPerMo)
		
#practice
#First, create another check minimum class function
#It should evaluate the P and K levels based on a crop input
        def checkMinWithInput(self, Pfert, Kfert, amount):
            self.P = int(self.getPvalue()) + int(Pfert * amount)
            self.K = int(self.getKvalue()) + int(Kfert * amount)
            if self.getPvalue() >= 140:
                print "P levels are adequate.  Current level: " + str(self.getPvalue())
            else:
                print "P levels are low.  Current level: " + str(self.getPvalue())
    
            if self.getKvalue() >= 90:
                print "K levels are adequate.  Current level: " + str(self.getKvalue())
            else:
                print "K levels are low.  Current level: " + str(self.getKvalue())

field7 = Soil("clay", 140, 50)

print(field7.basicType)
print(field7.P)
print(field7.K)
print(field7)

field8 = Soil("loam",120, 60)

print(field8.basicType)
print(field8.P)
print(field8.K)

print(field8)
print(field7)
print(field7.basicType)

newField = Soil("clay",100,70)
# Blue Sky Energy
# Lead Manager
# CRM Dialer API Integration
# Woody Hooten, 2020

from lead_scripts import *

people = [i for i in dialers]

while 1:
	person = input("Who needs some fresh leads?: ")

	try:
		dialers[person]
	except KeyError:
		print("Not a real dialer! \nYou can choose from the following: ")
		print(people, "\n")
		continue

	refreshLeads(person,dialers[person]['level'])

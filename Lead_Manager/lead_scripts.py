# ßrazen 5tudios
# CRM Dialer API Integration
# Maestro frymatic
# Woody Hooten, 2020

from crmdialerbot import *
from dialers import *
import time, datetime

filepath = 'leadslog.txt'  

nameGlobal = None
numberGlobal = None

# check notes on a lead, increment score 
def scrubNotes(leadId):
	notes = getLeadNotes(leadId)

	for note in notes.json()['data']:
		# print(note['text'])
		if 'created an appointment' in note['text']:
			print('follow up missed!')
			scrub['score'] += 1
			updateLead(leadId,93)  # status 93: follow up scheduled, decision
			# assignUser(leadId,66)
			# appts = getLeadAppts(leadId)
			# appointment = 

			return 1
		if 'Wrong number' in note['text']:
			print('DNC')
			scrub['score'] += 1
			updateLead(leadId,87)
			return 1
		if 'Do not call requested' in note['text']:
			print('DNC')
			scrub['score'] += 1
			updateLead(leadId,87)
			return 1
		if 'Spanish Speaker' in note['text']:
			print('Español')
			scrub['score'] += 1
			updateLead(leadId,97)
			return 1

	return None

# accepts a dict from dialers.py
# clear all dialing leads from a dialer
def wipeLeads(dialer):
	
	scrub['score'] = 0

	print(dialer)

	# get block of leads to be wiped
	leads = getDialerLeads(dialer['payload'],1000)
	leadList = leads.json()['data']

	# Unassign Dialer, Assign frymatic
	leadCount = 0
	scrub['wiped'] = len(leadList)
	for lead in leads.json()['data']:
		leadCount += 1

		#check for notes that include outcomes that need status updates
		strike = scrubNotes(lead['id'])
		if strike:
			print(dialer['name'] + " (" + str(leadCount) + " of " + str(scrub['wiped']) +"): lead id #" + str(lead['id']) + " cleared")
			continue
		unassignUser(lead['id'], dialer['id'])
		assignUser(lead['id'], dialers['frymatic']['id'])
		print(dialer['name'] + " (" + str(leadCount) + " of " + str(scrub['wiped']) +"): lead id #" + str(lead['id']) + " cleared")

	print("leads wiped! score", str(scrub['score']))
	return scrub['score']

# accepts a dict from dialers.py
# assign new leads to a dialer
def assignLeads(dialer,number):
	# Get 100 leads from Brayden (sort by oldest)
	newLeads = getDialerLeads(dialers['Brayden']['payload'],number)
	leadList = newLeads.json()['data']

	batch = []
	# assign if there are enough leads
	if len(leadList) == number:
		# Unassign Brayden, Assign Dialer
		leadCount = 0
		scrub['assigned'] = len(leadList)

		for lead in leadList:
			leadCount += 1
			batch.append(unassignUser(lead['id'], dialers['Brayden']['id']))
			batch.append(assignUser(lead['id'], dialer['id']))
			print(dialer['name'] + " (" + str(leadCount) + ") lead #" + str(lead['id']) + " assigned")
		
		print("new leads assigned")
		return None
	else:
		print("Brayden leads insufficient")
		return None
	

def refresh(user,number):
	# Confirm Request to Dialer
	print("leads refreshing")
	# discord.output("Lead refresh requested for " + dialer + ". Now in progress.")
	dialer = dialers[user]

	wiped = wipeLeads(dialer)
	assigned = assignLeads(dialer,number)



def refreshLeads(name, level):
	# get time stamp
	t = time.time()

	number = levels[level]

	# check that lead assignment request is proper
	if (number != 10 and number != 25 and number != 50 and number != 100):
		print("Please choose an amount of 10, 25, 50, or 100")
		return None

	#refresh leads

	refresh(name, number)

	print("assigning new leads")

	


	elapsed = time.time() - t

	print("time elapsed: ", elapsed)

	with open(filepath,'a') as leadLog:
		leadLog.write(str(datetime.date.today()) + ": "
			+ name + " leads refreshed (" + str(scrub['wiped'])
			+ " wiped, " + str(scrub['score']) + " status updates missed, " + str(scrub['assigned']) + " assigned) - runtime "
			+ str(elapsed) + " seconds.\n")

def scrubOutcomes(leadId):
	return None

def migrateLeads():
	return None

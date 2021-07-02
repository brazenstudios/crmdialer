# ßrazen 5tudios
# CRM Dialer API Integration
# Maestro frymatic
# Woody Hooten, 2020

import requests
import json
from crmd_token import *

# base url for leads

crmdUrl = 'https://bluesky.crmdialer.com/api/v1/'


# parameters for pulling leads
headers = {
	'accept':'application/json',
	'X-API-KEY':apiToken,
	'campaign':None,
	'status':None,
	'user':None,
}

##################################




##################################
# GETS
##################################

def getLeads():
	leadsUrl = crmdUrl + "leads"
	return requests.get(leadsUrl, headers=headers)

def getDialerLeads(userId,number):
	dialerLeadsUrl = crmdUrl + "leads"

	payload = {
		# "campaign":2,
		"status":12,
		"user":userId,
		"sort_by":"id",
		"per_page":number
	}

	return requests.get(dialerLeadsUrl, headers=headers, json=payload)

def getFields():
	fieldsUrl = crmdUrl + "leads/fields"
	return requests.get(fieldsUrl, headers=headers)

def leadDetails(leadId):
	leadIdUrl = crmdUrl + "leads/" + str(leadId)
	return requests.get(leadIdUrl, headers=headers)

def getLeadNotes(leadId):
	leadNotesUrl = crmdUrl + "leads/" + str(leadId)  + "/notes"
	return requests.get(leadNotesUrl, headers=headers)

def getLeadAppts(leadId):
	leadApptsUrl = crmdUrl + "leads/" + str(leadId)  + "/appointments"
	return requests.get(leadApptsUrl, headers=headers)

def getStatuses():
	return None

# get groups by dialing leads status
def getGroups():
	payload ={
		"status":12
	}

def getUsers():
	return None

def getTabs():
	tabsUrl = crmdUrl + "leads/fields/tabs"
	print(tabsUrl)
	return requests.get(tabsUrl, headers=headers)


##################################
# POSTS
##################################

# create form based on lead data
def populatePDF(leadId, appId):
	populatePdfURL = crmdUrl + "leads/" + str(leadId) + "/applications/" + str(appId) + "/populate"
	return requests.post(populatePdfURL, headers=headers)

# add user to 
def assignUser(leadId, userId):
	payload = {"user":userId}
	assignUserUrl= crmdUrl + "leads/" + str(leadId) + "/users"
	# print(assignUserUrl)
	return requests.post(assignUserUrl, headers=headers,json=payload)

# add note https://www.crmdialer.com/api/#/paths/~1leads~1{leadId}~1notes/post
def addNote(leadId):

	payload = {
		"tab":2,
		"note":"Skyler test API note",
		"sticky":"No"
	}

	addNoteUrl= crmdUrl + "leads/" + str(leadId) + "/notes"
	return requests.post(addNoteUrl, headers=headers,json=payload)

##################################
# PATCHES
##################################

def updateLead(leadId, status):
	payload = {
		"status":status,
	}

	leadUpdate = crmdUrl + "leads/" + str(leadId) 
	return requests.patch(leadUpdate, headers=headers, json=payload)





##################################
# DELETES
##################################

def unassignUser(leadId, userId):
	unassignUserUrl = crmdUrl + "leads/" + str(leadId) + "/users/" + str(userId)
	# print(unassignUserUrl)
	return requests.delete(unassignUserUrl, headers=headers)

# core loop
# counter = 0
# while crmd_url:
# 	counter += 1
# 	r = getem(crmd_url,headers)
	
# 	leads_json = r.json()['data']
# 	links = r.json()['links']
	
# 	crmd_url = links['next']
	
	# print(counter, ": ",len(leads_json), crmd_url)



# print(leads_json['data'])

# for 
# leads = r.json()

# print(len(leads['data']))


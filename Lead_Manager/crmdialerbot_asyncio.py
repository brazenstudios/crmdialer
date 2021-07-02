# Blue Sky Energy
# Lead Manager
# CRM Dialer API Integration
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

async def getLeads():
	leadsUrl = crmdUrl + "leads"
	return requests.get(leadsUrl, headers=headers)

async def getDialerLeads(userId,number):
	dialerLeadsUrl = crmdUrl + "leads"

	payload = {
		# "campaign":2,
		"status":12,
		"user":userId,
		"sort_by":"id",
		"per_page":number
	}

	return requests.get(dialerLeadsUrl, headers=headers, json=payload)

async def getFields():
	fieldsUrl = crmdUrl + "leads/fields"
	return requests.get(fieldsUrl, headers=headers)

async def leadDetails(leadId):
	leadIdUrl = crmdUrl + "leads/" + str(leadId)
	return requests.get(leadIdUrl, headers=headers)

async def getLeadNotes(leadId):
	leadNotesUrl = crmdUrl + "leads/" + str(leadId)  + "/notes"
	return requests.get(leadNotesUrl, headers=headers)

async def getLeadAppts(leadId):
	leadApptsUrl = crmdUrl + "leads/" + str(leadId)  + "/appointments"
	return requests.get(leadApptsUrl, headers=headers)

async def getStatuses():
	return None

# get groups by dialing leads status
async def getGroups():
	payload ={
		"status":12
	}

async def getUsers():
	return None

async def getTabs():
	tabsUrl = crmdUrl + "leads/fields/tabs"
	print(tabsUrl)
	return requests.get(tabsUrl, headers=headers)


##################################
# POSTS
##################################

# create form based on lead data
async def populatePDF(leadId, appId):
	populatePdfURL = crmdUrl + "leads/" + str(leadId) + "/applications/" + str(appId) + "/populate"
	return requests.post(populatePdfURL, headers=headers)

# add user to 
async def assignUser(leadId, userId):
	payload = {"user":userId}
	assignUserUrl= crmdUrl + "leads/" + str(leadId) + "/users"
	# print(assignUserUrl)
	return requests.post(assignUserUrl, headers=headers,json=payload)

# add note https://www.crmdialer.com/api/#/paths/~1leads~1{leadId}~1notes/post
async def addNote(leadId):

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

async def updateLead(leadId):
	leadUpdate = crmdUrl + "leads/" + str(leadId) 
	return requests.patch(leadUpdate, headers=headers)





##################################
# DELETES
##################################

async def unassignUser(leadId, userId):
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


#Team: Ganesh Byrandurga Gopinath, Deepak Kysarahalli Timmappa
from ciscosparkapi import CiscoSparkAPI, MembershipsAPI
import json
api = CiscoSparkAPI()

all_rooms = api.rooms.list()
demo_rooms = [room for room in all_rooms if ('wassup2' or 'wassup1') in room.title]
print len(demo_rooms)
room_list=[]
for room in demo_rooms:
	room_list.append(room.id)
room_dic = set(room_list)
room_list = list(room_dic)
print room_list
email_addresses = []
for id1 in room_list:
	mem = api.memberships.list(id1)
	for i in mem:
		email_addresses.append(i.personEmail)
email_set = set(email_addresses)
email_addresses = list(email_set)
print email_addresses
demo_room = api.rooms.create('newsampleroom4')
for email in email_addresses:
	if email != 'gaby6594@colorado.edu':
		try:
			api.memberships.create(demo_room.id, personEmail=email)
		except:
			pass

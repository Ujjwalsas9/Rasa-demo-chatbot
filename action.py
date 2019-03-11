from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import MySQLdb


# class ActionDb(Action):
# 	def name(self):
# 		return "action_db"
		
	# def run(self, dispatcher, tracker, domain):
	# 	import MySQLdb
	# 	db = MySQLdb.connect("localhost","root","Abcd_1234","DBforChatbot")
	# 	cursor = db.cursor()
	# 	idn = tracker.get_slot('personid')
	# 	sql = "select StockName, StockBalance from Persons WHERE PersonID = '%d';" % (idn)
	# 	try:
	# 		cursor.execute(sql)
	# 		if cursor.execute(sql)==0:
	# 			print("Sorry, could not find any relevant data. Please contact 1234 for further assistance.")
	# 		results = cursor.fetchall()
	# 		for row in results:
	# 			stockname = row[0]
	# 			stockbal = row[1]
	# 		# Now print fetched result
	# 		details = ("stockname=%s,stockbal=%d" % (stockname,stockbal))
	# 		response = """There are currently {} items available with the stock item {} at the moment.""".format(stockname, stockbalance)
	# 		dispatcher.utter_message(response)
	# 		return [SlotSet('personid',idn)]
	# 	except:
	# 		print ("Error: unable to fetch data")
	# 	finally:
	# 		db.close()

	# def run(self, dispatcher, tracker, domain):
	# 	import MySQLdb
	# 	print("hahahaha1")
	# 	db = MySQLdb.connect("localhost","root","Abcd_1234","DBforChatbot")
	# 	print("hahahaha2")
	# 	cursor = db.cursor()
	# 	print("hahahaha3")
	# 	idn = tracker.get_slot('personid')
	# 	print("hahahaha4")
	# 	q = "select * from restaurants where idn='{0}' limit 1".format(idn)
	# 	print("hahahaha5")
	# 	result = db.query(q)
	# 	return [SlotSet("matches", result if result is not None else [])]


	# def run(self, dispatcher, tracker, domain):
	# 	import MySQLdb
	# 	db = MySQLdb.connect("localhost","root","Abcd_1234","DBforChatbot")
	# 	cursor = db.cursor()
	# 	PersonID = tracker.get_slot('personid')
	# 	q = "select * from Persons where PersonID='{0}' limit 1".format(PersonID)
	# 	#result = db.query(q)
	# 	result = cursor.execute(q)
	# 	return [SlotSet("matches", result if result is not None else [])]

class ActionDb(Action):
	def name(self):
		return "action_db"

	def run(self, dispatcher, tracker, domain): 
		db = MySQLdb.connect("localhost","root","root","DBforChatbot")
		cursor = db.cursor()
		PersonID = tracker.get_slot('personid')
		q = "select StockName, StockBalance from Persons WHERE PersonID = '%d';" % (PersonID)
		try:
			cursor.execute(q)
			if cursor.execute(q)==0:
				print("Sorry, could not find any relevant data. Please contact 1234 for further assistance.")
			results = cursor.fetchall()
			#print("results: ", results)
			not all(results)
			for row in results:
				stockname = row[0]
				stockbal = row[1]
				# Now print fetched result
				details = ("stockname=%s,stockbal=%d" % (stockname,stockbal))
				print(details)
		except:
			print ("Error: unable to fetch data")
		finally:
			db.close()
        
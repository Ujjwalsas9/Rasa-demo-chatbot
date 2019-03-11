from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet



import MySQLdb
db = MySQLdb.connect("localhost","root","Abcd_1234","DBforChatbot")
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
# #result = db.query(q)
# result = cursor.execute(q)
# #return [SlotSet("matches", result if result is not None else [])]
# #[SlotSet("matches", result if result is not None else [])]
# print(result)




# # prepare a cursor object using cursor() method
# idn = 2
# db = MySQLdb.connect("localhost","root","Abcd_1234","DBforChatbot" )
# cursor = db.cursor()
# sql = "select StockName, StockBalance from Persons WHERE PersonID = '%d';" % (idn)
# try:
#     cursor.execute(sql)
#     if cursor.execute(sql)==0:
#         print("Sorry, could not find any relevant data. Please contact 1234 for further assistance.")
#     results = cursor.fetchall()
#     #print("results: ", results)
#     not all(results)
#     for row in results:
#         stockname = row[0]
#         stockbal = row[1]
#         # Now print fetched result
#         details = ("stockname=%s,stockbal=%d" % (stockname,stockbal))
#         print(details)
# except:
#     print ("Error: unable to fetch data")
# finally:
#     db.close()

    					         	Query with PyMongo
-------------------------------------------------------------------------------------------------------------------------------
from pymongo import MongoClient
client = MongoClient()

# client = MongoClient(host=['localhost:27017'])
# client = MongoClient(host=['mongodbserver:27017'])
# client = MongoClient(host=['197.24.2.19:27017'])

db = client.restaurant            # use restaurant.[restaurant is database name]

x = db.list_collection_names()     # similar as db.getCollectionNames()

for i in range(len(x)):
    c = x[i]
    d = db.get_collection(c)        # db.nameOfcollection
    for e in d.find():   # db.nameOfCollection.find(...)
        print(e)
------------------------------------------------------------------------------------------------------------------------------

import datetime
import pymongo
import pprint

from pymongo import  MongoClient,ASCENDING, DESCENDING
client= MongoClient()
db = client.restaurant            #similar as use restaurant
x= db.list_collection_names()     # db.getCollectionNames()
# print(x)
for i in range(len(x)):
    c = x[i]
    d = db.get_collection(c)      # db.nameofCollection()
    # for e in d.find()           # db.nameofCollection.find()
------------------------------------------------------------------------------------------------------------------------------
    
## 1) Write a MongoDB query to display all the documents in the collection restaurants.    
#     for e in d.find():
#         print(e)

##2) Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
    # for e in d.find({},{"restaurant_id": 1,"name": 1, "borough": 1, "cuisine": 1}):
    #     print(e)

##3)  Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.
    # for e in d.find({},{"restaurant_id": 1,"name": 1, "borough": 1, "cuisine": 1, "_id": 0}):
    #     print(e)

##4) Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
    # for e in d.find({},{"restaurant_id": 1, "name": 1, "borough": 1, "address.zipcode": 1, "_id": 0}):
    #     print(e)

##5) Write a MongoDB query to display all the restaurant which is in the borough Bronx.
    # for e in d.find({"borough": "Bronx"}):
    #     print(e)

##6)  Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.
    # for e in d.find({"borough": "Bronx"}).limit(5):
    #     print(e)
##7) Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
    # for e in d.find({"borough": "Bronx"}).skip(5).limit(5):
    #     print(e)

##8) Write a MongoDB query to find the restaurants who achieved a score more than 90.
    # for e in d.find({"grades.score": {"$gt":90}}):
    #     print(e)

##9)  Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.
    # for e in d.find({"grades.score": {"$gt" : 80, "$lt": 100}}):
    #     print(e)

##10) Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.
    # for e in d.find({"address.coord": {"$lt": -95.754168}}):
    #     print(e)

##11)Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.
    # for e in d.find({"$and" : [{"cuisine" : {"$ne" : "American "}}, {"address.coord.0" : {"$lt" : -65.754168}}, {"grades.score" : {"$gt" : 70}}]}):
    #     print(e)

##12) Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
#       Note : Do this query without using $and operator.
    # for e in d.find({ "cuisine" : {"$ne" : "American "}, "grades.score" :{"$gt": 70}, "address.coord" : {"$lt" : -65.754168}}):
    #     print(e)

##13) Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.

    # for e in d.find({"cuisine": {"$ne": "American "}, "grades.grade": "A", "borough": {"$ne": "Brooklyn"}}).sort([('cuisine', DESCENDING)]):
    #     pprint.pprint(e)

##14) Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.

    # for e in d.find({"restaurant_id":1, "name": 1, "borough": 1, "cuisine": 1}):
    #     print(e)

##17) Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish.

    # for e in d.find({"borough": "Bronx", "$or": [{"cuisine": "American ", "cuisine": "Chinese"}]}):
    #     print(e)

##18) Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.

    # for e in d.find({"borough": {"$in": ["Staten Island","Queens", "Bronx","Brooklyn"]}},{"_id":0,"restaurant_id":1,"name":1,"borough":1,"cuisine":1}):
    #     pprint.pprint(e)

##19)Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.

    # for e in d.find({"borough": {"$nin": ["Staten Island","Queens", "Bronx","Brooklyn"]}},{"_id":0,"restaurant_id":1,"name":1,"borough":1,"cuisine":1}):
    #     pprint.pprint(e)

##20) Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10.

    # for e in d.find({"grades.score": {"$not": {"$gt": 10}}},{"_id": 0,"restaurant_id":1,"name":1,"borough":1,"cuisine":1}):
    #     pprint.pprint(e)

##21) Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with letter 'Wil'. 
    
    # for e in d.find({"$or" : [{"name": /^Wil/},{"$and": [{"cuisine": {"$ne": "American "}},{"cuisine": {"$ne": "Chinees"}}]}]},{"restaurant_id": 1, "name":1, "borough":1, "cuisine":1}):
    #     pprint.pprint(e)

##22) Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISO Date "2014-08-11T00:00:00Z" among many of survey dates

    # for e in d.find({"grades.date": datetime.datetime(2014,8,11,0,0,0), "grades.grade": "A", "grades.score": 11},{"restaurant_id":1,"name":1,"grades":1}):
    #     pprint.pprint(e)

##23) Write a MongoDB query to find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z

    # for e in d.find({{"grades.1.date": datetime.datetime(2014,8,11,0,0,0), "grades.1.grade": "A", "grades.1.score": 9},{"restaurant_id":1,"name":1,"grades":1}}):
    #     pprint.pprint(e)

##24) Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52

    # for e in d.find({"address.coord.1": {"$gt": 42, "$lte": 52}},{"restaurant_id":1, "name":1,"address":1,}):
    #     pprint.pprint(e)

##25) Write a MongoDB query to arrange the name of the restaurants in ascending order along with all the columns.

    # for e in d.find().sort([('name', ASCENDING)]):
    #     pprint.pprint(e)

##26) Write a MongoDB query to arrange the name of the restaurants in descending along with all the columns.

    # for e in d.find().sort([('name',ASCENDING)]):
    #     pprint.pprint(e)




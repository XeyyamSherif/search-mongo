from pymongo import MongoClient, GEOSPHERE
import pymongo


def get_db():
    client = MongoClient(host='db',
                         port=27017, 
                         username='root', 
                         password='pass')
    database_mongo = client['database_1']
    return database_mongo

mydict = [
    {'location':{'type':"Point", 'coordinates': [-73.856077, 40.848447]}, "city":"Bakı", "street":"Naximov", "street number":"42"},
    {'location':{'type': "Point", 'coordinates': [ -73.9928, 40.7193 ]}, "street":"Samad Vurğun", "street number":"5"},
    {'location':{'type': "Point", 'coordinates': [ -73.9375, 40.8303 ]}, "city":"Gence", "street":"Tusi", "street number":"3"},
    {'location':{'type': "Point", 'coordinates': [ 40.393251, 49.857544 ]}, "city":"Baki", "street":"Cahangir Zeynalov", "street number":"45"},
    {'location':{'type': "Point", 'coordinates': [ 40.392687, 49.857833 ]}, "city":"Gence", "street":"Tabriz", "street number":"88"}
]

adress_table = get_db().adress_table

for item in mydict: 
    adress_table.insert_one(item)

adress_table.create_index([('city', pymongo.TEXT),('street', pymongo.TEXT),('street number', pymongo.TEXT)])
adress_table.create_index([("location", GEOSPHERE)])
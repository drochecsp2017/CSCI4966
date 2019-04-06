from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# retrieve the info from the database
client = MongoClient()
db = client.mongo_db_lab
collection = db.definitions


# Fetch one record
pprint.pprint(collection.find_one())
print("")

# Fetch a specific record
pprint.pprint( collection.find_one({"word": "De-rez"}) )
print("")

# Fetch a record by object id
pprint.pprint( collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b917")}) )
print("")

# Fetch all records
for words in collection.find():
    pprint.pprint( words )
print("")

# Insert a new record
new_word = {'definition': 'the cry of a CSCI4966 student hoping the insertion will be successful', 'word': 'insert pls'}
word_id = collection.insert_one(new_word).inserted_id
print(word_id)
print('\n')

if __name__ == '__main__':
    print "Modify me"


# imports
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import random
import datetime

# retrieve the info from the database
client = MongoClient()
db = client.mongo_db_lab
collection = db.definitions

id_list = []
for word_entry in collection.find():
    # add the word to our list of words
    id_list.append(word_entry["_id"])

    # initialize the list of dates to an empty list
    word_entry["dates"] = []
    collection.update({'_id':word_entry["_id"]}, {"$set": word_entry}, upsert=False)

# get some random word
def random_word_requester():
    # find the world to be randomly chosen
    index = random.randint(0, len(id_list) - 1)
    word_id = id_list[index]
    word_entry = collection.find_one({"_id": word_id})

    # log in the MongoDB database the timestamp that it was accessed.
    collection.update_one({'_id':word_id}, {"$set": {"word_entry.dates": word_entry["dates"].append(datetime.datetime.utcnow())}} )

    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    return word_entry


if __name__ == '__main__':
    entry = random_word_requester()
    print "word: " + entry["word"]
    print "definition: " + entry["definition"]
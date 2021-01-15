from pymongo import MongoClient

client = MongoClient('test-mongodb', 27017)
db = client.container_test
test_data = db.test_data

def save_data(data):
    document_id = test_data.insert_one(data)
    return document_id
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Access a database
db = client["my_database"]
collection = db["users"] # access the collection “user”

collection.insert_one({
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
})

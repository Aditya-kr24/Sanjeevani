from pymongo import MongoClient
MONGO_URI = "mongodb://localhost:27017/chatbot_db"


client = MongoClient(MONGO_URI)
db = client["chatbot_db"]

from pymongo import MongoClient

uri = "mongodb+srv://kaleshubham8459_db_user:SDVH3NKcB130mdZ@cluster0.ghdrmwf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

print(client.admin.command("ping"))
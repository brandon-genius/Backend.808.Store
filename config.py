
import pymongo
import certifi

con_str = "mongodb+srv://britt273:Hawaii2019@cluster0.j9pqq.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("808RunnerStore")
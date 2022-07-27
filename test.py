import pymongo

client = pymongo.MongoClient("mongodb+srv://codelearn:#CodeLearn43#@learncode.2ecxp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"faiz",
    "email":"codelearn@gmail.com",
    "surname":"nawab"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
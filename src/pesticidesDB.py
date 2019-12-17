from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd
import json

# Get Password
load_dotenv()
password = os.getenv('key')
connection = 'mongodb+srv://root:{}@cluster0-rad7h.mongodb.net/test?retryWrites=true&w=majority'.format(password)
print('Connected to DB!')
# Connect to DB
client = MongoClient(connection)

def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll


# collections
db, coll = connectCollection('Leaf_diseases', 'Pesticides')


#uploading data to Mongo Atlas
'''
df = pd.read_csv('./Input/ListadoProductos_2019_12_16-22_37.csv')
df.to_json('./Output/pesticides.json',orient='records')                               

with open('./Output/pesticides.json') as f:
    pesticides = json.load(f)
coll.insert_many(pesticides)'''

def get_pesticides(ai):
    '''Returns the pesticides which contain the specified ai'''

    results = coll.find({'Ai': ai},{'_id':0,})
                             
    return results


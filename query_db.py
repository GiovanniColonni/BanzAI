import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')

DomainData = client["Domain_Data"] 

Movies_collection = DomainData["Movies"]
TvSeries_collection = DomainData["TvSeries"]

def q1(): # film da 2010 a oggi
    
    start = datetime(2010,1,1,0,0,0)
    start = start.isoformat()
    
    print(start)
    
    q1_ = {"release_date":{"$gte": "2010-01-01"}}
    res = Movies_collection.find(q1_)
    
    for r in res:
        print(r)
       
if __name__ == "__main__":
    q1()
    
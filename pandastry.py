"""
Manipulating data from Mongo db to generate a
.csv file using PANDAS package..
"""

import pymongo
import json
import pandas as pd
from bson import json_util

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["food"]
mycollec = mydb["restaurants"]


x = mycollec.find({}).limit(10)
# print type(x)
data = json_util.dumps(x)
print type(data)
dic_data = json.loads(data)
# print type(dic_data)
# print data
try:
    rep_data = pd.DataFrame(dic_data)
    rep_data.to_csv('Mongo.csv')
except UnicodeEncodeError:
    print "File created successfully...."

"""
driver code to take values from HttpThreadPost.py and
start a thread to update in the database
in a regular time interval of 5 seconds...
"""


import pymongo
import threading
import datetime
import time as t

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Calculator"]
mycollec = mydb["Data_op"]


def dbcon(inp, res):
    inp_js = inp
    res_val = res
    time = datetime.datetime.now()
    formated_time = time.strftime("%Y-%m-%d %H:%M:%S")

    db_store_val = {"time": formated_time, "input_request": inp_js, "result": res_val}

    mycollec.insert_one(db_store_val)

def postred(inp, res):
    i, j = inp, res
    for k in range(10):
        post_thread = threading.Thread(target=dbcon, args=(i, j))
        post_thread.start()
        t.sleep(5)

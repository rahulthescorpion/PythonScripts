"""
Flask Application with HTTP methods
deals with Mongo Db

GET -- fetch everything from the db (User)

        input : { "find_data": "all"  }

POST -- it will add data in the database
        use any JSON input


PUT -- it will update the existing data in the database.

        input format :  { "old": { "field_name" : value }, "new": { "field_name": value  } }

        it will search for the field name in "old" in the DB and update it with new one..


DELETE -- it will delete the data in the datebase

        input format : { "name": "any_value to delete the record"  }

        if will give { 'name' : "credentials"} it will drop the collection

"""

from flask import Flask, request, jsonify
from bson import json_util
import pymongo
import json

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["User"]
mycollec = mydb["credentials"]


@app.route('/GET', methods=['GET'])
def get():
    result = []
    try:
        find = json.loads(request.data)
        ser = find.get("find_data")
        if find.get("find_data") != "all":      #
            a = mycollec.find_one(ser)
            res = json_util.dumps(mycollec.find_one(ser))
            return res
            #return jsonify(d)
        else:                                   #
            for i in mycollec.find():
                ret_data = json_util.dumps(i)
                man_data = json.loads(ret_data)
                del man_data["_id"]

                result.append(man_data)
            # return jsonify(ret_data)
            return jsonify(result)
    except:
        return "no data found.."


@app.route('/POST', methods=['POST'])
def post():
    req_data = request.data
    # list_d = [req_data]
    mycollec.insert_one(json.loads(req_data))
    return "record created successfully.."


@app.route('/PUT', methods=['PUT'])
def put():
    upd_rec = json.loads(request.data)
    old_rec = upd_rec.get("old")
    new_rec = upd_rec.get("new")
    mycollec.update(old_rec, new_rec)
    return "record updated successfully.."


@app.route('/DELETE', methods=['DELETE'])
def delete():
    del_data = json.loads(request.data)
    del_name = del_data.get("name")
    try:
        if del_name == "credentials":
            mycollec.drop()
            return "Data deleted completely"
        else:
            mycollec.delete_many(del_data)
            return "Specified data deleted successfully.."
    except:
        return "No data found.."


if __name__ == '__main__':
    app.debug = True
    app.run()

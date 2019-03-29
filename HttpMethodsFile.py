"""
Flask app with HTTP methods

Request will be received and processed
with HTTP methods to create a file..

GET -- it will written "python"
POST -- it takes the request and created a file with it.
        use input  format JSON.

        eg: {'name' : "python"}

PUT -- it will take the request and over write the same file

PATCH -- it will take the request and append it in the same file

DELETE -- it will delete the file...use input as

            { "file_name" : "filename with extension" }
"""

from flask import Flask, request
import os
import json

app = Flask(__name__)


@app.route('/GET', methods=['GET'])
def get():
    return "python"


@app.route('/POST', methods=['POST'])
def post():
    result = request.data
    _file = open('new.txt', "w+")
    _file.write(result)
    path = os.getcwd()
    return "file created successfully in the path"+" "+path


@app.route('/PUT', methods=['PUT'])
def put():
    res = request.data
    _file = open('new.txt', "w")
    _file.write(res)
    return "file over writed successfully..."


@app.route('/DELETE', methods=['DELETE'])
def delete():
    del_data = request.data
    file_name = json.loads(del_data)
    name = file_name.get("file_name")
    if os.path.exists(name):
        os.remove(name)
        return "File deleted successfully.."
    else:
        return "file not exits.."


@app.route('/PATCH', methods=['PATCH'])
def patch():
    patch = request.data
    _file = open('new.txt', "a")
    _file.write(patch)
    return "file updated successfully..."


if __name__ == '__main__':
    app.debug = True
    app.run()

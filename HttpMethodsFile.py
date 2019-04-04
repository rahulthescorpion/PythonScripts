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
import logging
from flasgger import Swagger

app = Flask(__name__)
swag = Swagger(app)
logging.basicConfig(filename="httpflask.log",
                    format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG,
                    filemode='a')
logging.info("---------------Application started----------------")


@app.route('/GET', methods=['GET'])
def get():
    """GET endpoint returning a string.
        This is using docstrings for specifications.
        ---
        definitions:
          GET:
            type: object
        responses:
          200:
            description: it will return python
        """
    return "python"


@app.route('/POST', methods=['POST'])
def post():
    """POST endpoint create a file with the data given.
            This is using docstrings for specifications.
            ---
            parameters:
              - name: POST
                in: body
                type: string
                required: false
                default: all
            definitions:
              POST:
                type: object
            responses:
              200:
                description: it will create a file with the data given
            """
    result = request.data
    if result:
        _file = open('new.txt', "w+")
        _file.write(result)
        path = os.getcwd()
        logging.info("POST request received..")
        logging.debug("Input data %s" % type(result))
        logging.debug(result)
        logging.info("Data saved successfully..")
        return "file created successfully in the path"+" "+path
    else:
        logging.info("GET request received..")
        logging.error("No input Given..")
        return "No input given.."


@app.route('/PUT', methods=['PUT'])
def put():
    """PUT over writes the data.
                This is using docstrings for specifications.
                ---
                parameters:
                  - name: PUT
                    in: body
                    type: string
                    required: false
                    default: all
                definitions:
                  PUT:
                    type: object
                responses:
                  200:
                    description: it will over writes the file
                """
    res = request.data
    if res:
        _file = open('new.txt', "w")
        _file.write(res)
        logging.info("PUT request received..")
        logging.info("file overwrited successfully..")
        return "file over writed successfully..."
    else:
        logging.info("PUT request received..")
        logging.error("No input given..file emptied..")
        return "No input given.."


@app.route('/DELETE', methods=['DELETE'])
def delete():
    """DELETE endpoint will delete the file.
                This is using docstrings for specifications.
                ---
                parameters:
                  - name: file_name
                    in: body
                    type: application/json
                    required: false
                    default: all
                definitions:
                  DELETE:
                    type: object
                responses:
                  200:
                    description: it will delete the file with the data given
                """
    del_data = request.data
    file_name = json.loads(del_data)
    name = file_name.get("file_name")
    if os.path.exists(name):
        os.remove(name)
        logging.info("DELETE request received..")
        logging.info("File deleted successfully..")
        return "File deleted successfully.."
    else:
        logging.info("DELETE request received..")
        logging.error("File not exits..")
        return "file not exits.."


@app.route('/PATCH', methods=['PATCH'])
def patch():
    """PATCH endpoint append the data into the file.
                This is using docstrings for specifications.
                ---
                parameters:
                  - name: PATCH
                    in: body
                    type: string
                    required: false
                    default: all
                definitions:
                  PATCH:
                    type: object
                responses:
                  200:
                    description: Data appended succcessfully..
                """
    patch = request.data

    if patch:
        _file = open('new.txt', "a")
        _file.write(patch)
        logging.info("PATCH request received..")
        logging.info("file updated successfully...")
        return "file updated successfully..."
    else:
        logging.info("PATCH request received..")
        logging.error("No input given..")
        return "No input given.."


if __name__ == '__main__':
    app.debug = True
    app.run()

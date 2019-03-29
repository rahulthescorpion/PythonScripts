"""
Flask App with POST API to process a simple
arithmetic operation in mango db using thread.

POST -- it will take two arguments along with operation

        eg: { "operation": "add", "value1": 5, "value2": 6}

        The data will be processed by a thread and given to
        postred method in HttpThreadDrive.py file..it will update the
        data in DB in regular interval of 5 seconds for 10 times..

"""


from flask import Flask, request
import json
import HttpThreadDrive
import threading

app = Flask(__name__)


@app.route('/POST', methods=['POST'])
def post():
    # res_st = "Request received successfully.."
    req = json.loads(request.data)
    op = req.get("operation")
    val1 = req.get("value1")
    val2 = req.get("value2")

    thread = threading.Thread(target=operate, args=(req, op, val1, val2))
    thread.start()
    return "request processed.."


def operate(req, op, val1, val2):
    if op == "add":
        res_d = val1 + val2
        HttpThreadDrive.postred(req, res_d)
        # return res_st
    elif op == "sub":
        res_d = val1 - val2
        HttpThreadDrive.postred(req, res_d)
        # return res_st
    elif op == "mul":
        res_d = val1*val2
        HttpThreadDrive.postred(req, res_d)
        # return res_st
    elif op == "div":
        res_d = val1/val2
        HttpThreadDrive.postred(req, res_d)
        # return res_st
    else:
        return "Operation not available.."


if __name__ == '__main__':
    app.debug = True
    app.run()



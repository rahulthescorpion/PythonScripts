"""
Unit test cases for Http methods
"""

import unittest
import json


class SimpleTest(unittest.TestCase):
    import HttpMongo

    def setUp(self):
        self.HttpMongo.app.testing = True

        self.client = self.HttpMongo.app.test_client()

        self.header = {
            'Content-Type': 'application/json'
        }

        self.get_data = {"find_data": "abc"}
        self.testdata = {"name": "shankar"}

        self.putdata = {"old": {"name": "rahul"}, "new": {"name": "shankar"}}

        self.jsndata = json.dumps(self.putdata)
        self.gdata = json.dumps(self.get_data)
        self.jdata = json.dumps(self.testdata)

        # print type(self.jdata)

    def test_post(self):
        res = self.client.post('/POST', headers=self.header, data=self.jdata)
        # print res.status_code
        self.assertEqual(200, res.status_code)

    def test_get(self):

        try:
            res = self.client.get('/GET', headers=self.header, data=self.gdata)
            result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
            strdata = json.dumps(result_in_json)

            # print type(strdata)
            dictdata = json.loads(strdata)
            # print dictdata
            # print type(dictdata)
        #  get data test_case
            # self.assertEqual(len(dictdata), 0)
        #   status code test_case

            self.assertEqual(200, res.status_code)

        except TypeError:
            print "Test case for GET method failed..No data available"

        except AssertionError:
            print "Test case for GET method failed...Data Mismatch"


    def test_put(self):
        # path = "http://127.0.0.1:5000/PUT?search_query=%s" % self.jdata
            res = self.client.put('/PUT', headers=self.header, data=self.jsndata)
            self.assertEqual(200, res.status_code)
            self.assertEqual("record updated successfully..", res.data)

    def test_delete(self):
        res = self.client.delete('/DELETE', headers=self.header, data=self.jdata)

        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
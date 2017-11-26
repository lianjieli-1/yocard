# -*- coding:utf-8 -*-
import requests
import unittest

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.sojson.com/open/api/weather/json.shtml?"
        self.data = {'city':'北京'}

    def test_get_acitvity(self):
        result = requests.get(self.url,self.data)
        data = result.json()
        self.assertEqual(data['status'],200)

    def test_get_city(self):
        data = {'city':''}
        result = requests.get(self.url,data)
        data = result.json()
        self.assertEqual(data['status'],304)

if __name__ == "__main__":
    unittest.main()

# basemodel.py

import web, json, os, sys

class BaseModel:
	def get_data(self):
		json_data = open('thucydides.json')
		data = json.load(json_data)
		return data

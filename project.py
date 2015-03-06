import json, basemodel
from pprint import pprint

all_data = basemodel.BaseModel().get_data()

all_projects = all_data[1]['projects']

class Project:

	def __init__(self):
		self.id = None
		self.title = None
		self.description = None

	def find_all(self):
		return all_projects

	def find(self, key, value):
		projects_found = [project for project in all_projects if project[key] == value]
		return projects_found

	def find_one(self, key, value):
		project_found = [project for project in all_projects if project[key] == value]
		return project_found[0]


p = Project()

print(p.find_one("id", 1))
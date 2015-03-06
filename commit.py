#commit.py

import json, basemodel
from pprint import pprint

all_data = basemodel.BaseModel().get_data()

all_commits = all_data[0]['commits']
all_projects = all_data[1]['projects']

class Commit:

	def __init__(self):
		self.project_id = None
		self.commit_title = None
		self.date = None
		self.markdown = None

	def find_all(self):
		y = [commit for commit in all_commits if commit['project_id'] == 1]
		return y

	def find(self, index, key, value):
		return all_commits[index].get(key, value)

	def find_one(self, index, key):
		return all_commits[index][key]

x = Commit()

print(all_commits)

print(x.find_all())

class Project:

	def __init__(self):
		self.id = None
		self.title = None
		self.description = None

	def find_all(self):
		return all_projects

	#def find(self, key):

	#def find_one(self, index, key):



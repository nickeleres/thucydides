#commit.py

import json, basemodel
from pprint import pprint

all_data = basemodel.BaseModel().get_data()

all_commits = all_data[0]['commits']

class Commit:

	def __init__(self):
		self.project_id = None
		self.commit_title = None
		self.date = None
		self.markdown = None

	def find_all(self):
		return all_commits

	def find(self, key, value):
		commits_found = [commit for commit in all_commits if commit[key] == value]
		return commits_found

	def find_one(self, key, value):
		commit_found = [commit for commit in all_commits if commit[key] == value]
		return commit_found[0]

x = Commit()

#print(x.find_one('project_id', '1'))













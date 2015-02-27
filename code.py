#app.py
#! /usr/bin/python
import json
from pprint import pprint
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web

render = web.template.render('templates/')

#maps URLs to classes
urls = (
	'/commits', 'commits'
)
#defines the class methods associated with URL end points
class commits:
	def GET(self):
		#project = 'greenglass'
		#commit = ['commit1', 'commit2', 'commit3']
		#return render.commits(project, commit)
		json_data = open('thucydides.json')
		data = json.load(json_data)
		return render.commits(data)

#creates application and specifies the use of above URLs
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()    



#calls mod_wsgi
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

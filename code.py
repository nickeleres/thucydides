#app.py
#! /usr/bin/python

import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web

render = web.template.render('templates/')

#maps URLs to classes
urls = (
	'/commits', 'index'
)
#defines the class methods associated with URL end points
class index:
	def GET(self):
		#i = web.input(name=None)
		project = 'greenglass'
		commit = ['commit1', 'commit2', 'commit3']
		return render.commits(project, commit)

#creates application and specifies the use of above URLs
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()    


#calls mod_wsgi
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

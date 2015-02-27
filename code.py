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
	'/commits', 'commits',
	'/new', 'new',
	'/login', 'login'
)
#defines the class methods associated with URL end points
class commits:
	def GET(self):
		json_data = open('thucydides.json')
		data = json.load(json_data)
		return render.commits(data)

class new:
    def GET(self):
    	form = self.form()
    	return render.new(form) 

    def POST(self):
    	form = self.form()
    	if not form.validates():
    		return render.new(form)
    	model.new_post(form.d.title, form.d.date, form.d.entry)
    	raise web.seeother('/')

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            size=30,
            description="Post title:"),
        web.form.Textbox('date', web.form.notnull, 
            size=30,
            description="Post date & time:"),
        web.form.Textarea('content', web.form.notnull, 
            rows=30, cols=80,
            description="Post content:"),
        web.form.Button('commit entry'),
    )

class login:
	def GET(self):
		login = form.Form(
		    form.Textbox('username'),
		    form.Password('password'),
		    form.Button('Login'),
		)
		l = login()
		return render.login(l)

#creates application and specifies the use of above URLs
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()    



#calls mod_wsgi
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

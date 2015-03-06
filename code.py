# #defines the class methods associated with URL end points
# class Commits:
# 	def GET(self):
# 		data = basemodel.BaseModel().get_data()
# 		return render.commits(data)


import web, json, sys, os, basemodel
from pprint import pprint

render = web.template.render('/Users/argenticdev/mySites/Thucydides/templates')

urls = (
  '/', 'Hello',
  '/commits', 'Commits',
  '/new', 'New'
  )

class Hello:
	def GET(self):
		basemodel_instance = basemodel.BaseModel()
		commit_instance = commit.Commit()
		all_commits = commit_instance.findAll()
		return render.commits(all_commits)

class Commits:
	def GET(self):
		basemodel_instance = basemodel.BaseModel()
		all_commits = basemodel_instance.get_data()
		return render.commits(all_commits)

class New:
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


def application(environ, start_response):
    # Wrapper to set SCRIPT_NAME to actual mount point.
    os.environ['ROOT_PATH'] = environ.get('ROOT_PATH')
    return _application(environ, start_response)


application = web.application(urls, globals()).wsgifunc()


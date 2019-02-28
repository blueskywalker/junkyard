import os, os.path
import random
import string
import json
import cherrypy


@cherrypy.expose
class MobileyeWebService(object):

    @cherrypy.tools.json_out()    
    def GET(self):
        return "okay"

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        jsondata = cherrypy.request.json
        print jsondata
        return jsondata

    # def PUT(self, another_string):
    #     cherrypy.session['mystring'] = another_string

    # def DELETE(self):
    #     cherrypy.session.pop('mystring', None)


@cherrypy.expose
class HelloWorld(object):

    def GET(self):
        return "hello"


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    
    cherrypy.quickstart(MobileyeWebService(), '/request', conf)



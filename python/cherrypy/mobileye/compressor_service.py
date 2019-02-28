
from multiprocessing import JoinableQueue, Process
import cherrypy
import simplejson

@cherrypy.expose

class MobileyeImageCompressor(object):

    def __init__(self, queue):
        self.queue = queue

    @cherrypy.tools.json_out()
    def GET(self):
        return "okay"


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        print(cherrypy.request.json)



if __name__ == "__main__":
    conf = {
        '/' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')]
        },
        'global': {
            'server.socket_host' : '0.0.0.0'
         }
    }

    mobileye = MobileyeImageCompressor(JoinableQueue())
    cherrypy.quickstart(mobileye, '/', conf)
    

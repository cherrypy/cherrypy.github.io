import os

import cherrypy
from cherrypy.lib.static import serve_file


class Site(object):
    @cherrypy.expose
    def index(self):
        return serve_file(os.path.join(os.getcwd(), 'index.html'))

    @classmethod
    def run(cls):
        config = {
            '/images': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.join(os.getcwd(), 'images'),
            },
            '/js': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.join(os.getcwd(), 'js'),
            },
            '/css': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.join(os.getcwd(), 'css'),
            },
        }
        cherrypy.quickstart(cls(), config=config)


__name__ == "__main__" and Site.run()

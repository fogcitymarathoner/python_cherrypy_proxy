import cherrypy
import requests

class Proxy(object):
    @cherrypy.expose
    def index(self, url=None):

        r = requests.get(url)

        return r.text


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '192.168.1.7',
        'server.socket_port': 8080,
        'tools.encode.encoding': "utf-8",
    })
    cherrypy.quickstart(Proxy())
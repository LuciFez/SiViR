import sys
from controller.controllerInstagramApi import instagramAPI

sys.path.append('../')

def controllerFirstPage(environ, start_response):
    start_response('200 OK', [('Content-text', 'text/html')])
    file = open("view/firstPage/firstPage.html", "r").read()
    yield file.encode('utf-8')
    instagramAPI()



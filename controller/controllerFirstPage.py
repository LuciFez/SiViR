import sys
from model.util import checkJWT
sys.path.append('../')


def controllerFirstPage(environ, start_response):
    start_response('200 OK', [('Content-text', 'text/html')])
    if checkJWT(environ):
        response = open("view/firstPage/firstPage.html", "r").read()
    else:
        response = open('view/login/login.html', 'r').read()
    yield response.encode('utf-8')



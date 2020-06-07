import cgi
from Controllers.register import *
from Controllers.loginController import *
from Controllers.publicKeyController import *


def notfound(environ, start_response):
    start_response('404 Not Found', [('Context-type', 'text/plain')])
    return [b'404 Not Found']


def handleIMG(environ, start_response):
    path = environ['PATH_INFO']
    try:
        response = open("Views/" + path, "rb").read()

        start_response('200 OK', [('content-type', 'image/png')
            , ('content-length', str(len(response)))])
        return [response]
    except IOError:
        print(path)
        return notfound(environ, start_response)


def handleCSS(environ, start_response):
    path = environ['PATH_INFO']
    start_response('200 OK', [('Content-text', 'text/css')])
    response = open('Views' + path, 'rb').read()
    yield response


def handleHTMLandJS(environ, start_response):
    path = environ['PATH_INFO']
    start_response('200 OK', [('Content-text', 'text/html')])
    response = open('Views' + path, 'rb').read()
    yield response


class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {k: params.getvalue(k) for k in params}
        if path.endswith(".jpg") or path.endswith(".png"):
            return handleIMG(environ, start_response)
        elif path.endswith(".html") or path.endswith("js"):
            return handleHTMLandJS(environ, start_response)
        elif path.endswith(".css"):
            return handleCSS(environ, start_response)
        else:
            handler = self.pathmap.get((method, path), notfound)
            return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function


def index(environ, start_response):
    start_response('200 OK', [('Content-text', 'text/html')])
    response = open('Views/main.html', 'r').read()
    yield response.encode('utf-8')


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', index) #
    dispatcher.register('POST', '/signup', controllerSignUpPOST)
    dispatcher.register('GET', '/signup', controllerSignUpGET)
    dispatcher.register('GET', '/login', loginGET)
    dispatcher.register('GET', '/getkey', controllerGetPubKey)
    httpd = make_server('localhost', 8000, dispatcher)
    httpd.serve_forever()

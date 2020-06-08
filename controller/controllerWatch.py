import sys
import json
sys.path.append('../')
from model.util import checkJWT
from model.watch import *


def controllerWatch(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Bad username or password"}
        yield json.dumps(message).encode('utf-8')
    if 'v' in params:
        start_response('200 OK', [('Content-text', 'text/plain')])
        template = open("view/watch/watch.html", "r").read()
        id = params['v']
        video = videoPlayer(id)
        html = template.format(id=id, title=video['title'], description=video['description'])
        yield html.encode('utf-8')
    else:
        start_response("400 Bad Request", [('Content-text', 'text/plain')])
        message = {"message": "Empty query"}
        yield json.dumps(message).encode('utf-8')
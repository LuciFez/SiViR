import sys
import json
sys.path.append('../')
from model.youtubeAPI import *
from model.util import checkJWT

def controllerRecommendations(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Bad username or password"}
        yield json.dumps(message).encode('utf-8')
    else :
            videos = {'videos': getRecommendation()}
            start_response('200 OK', [('Content-text', 'text/plain')])
            yield json.dumps(videos).encode('utf-8')

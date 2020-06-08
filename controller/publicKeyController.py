import sys
sys.path.append('../')
from model.pubicKey import *

def controllerGetPubKey(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/x-pem-file')])
    response = getPubKey()
    yield response

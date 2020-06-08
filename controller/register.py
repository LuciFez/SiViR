import sys
import json
sys.path.append('../')
from model.signUp import *


def controllerSignUpPOST(environ, start_response):
    params = environ['params']
    response = sing_up(params["uname"], params["passw"], params["fname"], params["lname"])
    start_response(response, [('Content-text', 'text/plain')])
    if response == "201 Created":
        message = {"message": "Success!"}
    elif response == "400 Bad Request":
        message = {"message": "Bad ceva"}
    else:
        message = {"message": "Nu stiu inca"}
    yield json.dumps(message).encode('utf-8')


def controllerSignUpGET(environ, start_response):
    start_response('200 OK', [('Content-text', 'text/html')])
    response = open('view/signup/sign_up.html', 'r').read()
    yield response.encode('utf-8')

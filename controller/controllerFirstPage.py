import sys
from http.cookies import SimpleCookie
sys.path.append('../')
from model.util import *
from model.login import *
import jwt
import json


def controllerFirstPage(environ, start_response):
    start_response('200 OK', [('Content-text', 'text/html')])
    file = open("view/firstPage/firstPage.html","r").read()
    yield file.encode('utf-8')
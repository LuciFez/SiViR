import sys
from http.cookies import SimpleCookie
sys.path.append('../')
from model.util import *
from model.login import *
import jwt
import json
from datetime import datetime, timezone


def loginGET(environ, start_response):
    unfromated_cookie = environ.get("HTTP_COOKIE","")
    cookie = SimpleCookie()
    cookie.load(unfromated_cookie)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value


    passw = cookies['passw']
    uname = cookies['uname']
    passw = decript(passw)
    login_status = login(uname, passw)
    if login_status == 1:
        start_response('200 OK', [('Content-text', 'text/plain')])
        encoded_jwt = jwt.encode({'uname': uname, 'iat': datetime.utcnow()}, 'secret', algorithm='HS256')
        message = {"jwt": encoded_jwt.decode('utf-8')}
        yield encoded_jwt
    elif login_status == 2:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Bad username or password"}
        yield json.dumps(message).encode('utf-8')
    elif login_status == 3:
        start_response("500 Internal Server Error", [('Content-text', 'text/plain')])
        message = {"message": "Databease problem"}
        yield json.dumps(message).encode('utf-8')


    
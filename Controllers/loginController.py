import sys
from http.cookies import SimpleCookie
sys.path.append('../')
from Models.util import *
from Models.login import *
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
    if login(uname, passw):
        start_response('200 OK', [('Content-text', 'text/plain')])
        iat = datetime.now(timezone.utc).timestamp()
        encoded_jwt = jwt.encode({'uname': uname, 'iat': iat}, 'secret', algorithm='HS256')
        print(encoded_jwt)
        return encoded_jwt

    else:
        start_response('403 Forbidden', [('Content-text', 'text/plain')])
        message = {"message": "Nu stiu inca"}

    yield json.dumps(message).encode('utf-8')
    
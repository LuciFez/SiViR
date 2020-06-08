from http.cookies import SimpleCookie
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
import jwt


def decript(encrypted):
    key = RSA.importKey(open("myKey.pem").read())
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    decrypted_message = cipher.decrypt(b64decode(encrypted))
    return decrypted_message.decode("utf-8")

def checkJWT(environ):
    cookies = getCookies(environ)

    if 'jwt' in cookies:
        encoded = cookies['jwt']
        key = 'secret'
        try:
            payload = jwt.decode(encoded, key, algorithm='HS256', options={'require': ['uname', 'iat']})
            return payload['uname']
        except jwt.DecodeError:
            return False
    else:
        return False

def getCookies(environ):
    unfromated_cookie = environ.get("HTTP_COOKIE", "")
    cookie = SimpleCookie()
    cookie.load(unfromated_cookie)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import random
from base64 import b64decode,b64encode

def decript(encrypted):
    print(encrypted)
    key = RSA.importKey(open("myKey.pem").read())
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    decrypted_message = cipher.decrypt(b64decode(encrypted))
    return decrypted_message.decode("utf-8")

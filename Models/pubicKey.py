from Crypto.PublicKey import RSA

def getPubKey():
    return RSA.importKey(open("myKey.pem").read()).publickey().exportKey()

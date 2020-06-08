from Crypto.PublicKey import RSA

keyPair = RSA.generate(2048)

f = open("../myKey.pem", 'wb')
f.write(keyPair.exportKey('PEM'))
f.close()

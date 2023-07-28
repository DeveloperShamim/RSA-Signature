import rsa

def genarate_keys():
    (publicKey, PrivateKey) = rsa.newkeys(1024)
    with open('publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privateKey.pem', 'wb') as p:
        p.write(PrivateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-256')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key, ) == 'SHA-256'
    except:
        return False





genarate_keys()


private_Key, public_Key = loadKeys()

message = input('Write your message here:')
digital_signature = sign(message, private_Key)

print("This is the signature ----------------------------------------------------------")
print(digital_signature)

print("This is the verification step ----------------------------------------------------")
print(verify(message,digital_signature,public_Key))



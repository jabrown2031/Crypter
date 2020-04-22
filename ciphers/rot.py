# Rotation cipher
# rot 13 and ceaser
# uses UTF-8 or UTF-16 charater sets

import binascii

def encrypt(plaintext, key):
    ciphertext = b'';
    shift=0;
    
    for i in range(len(plaintext)):
        if ((ord(plaintext[i]) + key) <= 65535):
            ciphertext += binascii.unhexlify(hex(ord(plaintext[i]) + key).strip('0x').encode());
        else:
            ciphertext += binascii.unhexlify(hex(ord(plaintext[i]) + (65535 - key).strip('0x').encode());


    return ciphertext;

def decrypt(ciphertext, key):


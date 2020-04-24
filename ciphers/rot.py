# Rotation cipher
# rot 13 and ceaser
# uses UTF-16 charater sets

## encrypt text with a shift of key
## generate a HEX string
def encrypt(plaintext, key):
    ciphertext = "";
    c = 0;

    for i in range(len(plaintext)):
        c = ord(plaintext[i]) + key;

        # if shift is at edge of char space
        # start at 0
        # if shift is negative
        # start at 65536
        if (c >= 65536):
            c = c - 65536;
        elif (c < 0):
            c = c + 65536;

        ciphertext += hex(c);

    return ciphertext;

## decrypt text with a shift of key
## generate a CHAR string
def decrypt(ciphertext, key):
    plaintext = "";
    c = 0;

    for i in range(1, len(ciphertext.split('0x'))):
        c = int(ciphertext.split('0x')[i], 16) - key;

        # if shift is at edge of char space
        # start at 0
        # if shift is negative
        # start at 65536
        if (c >= 65536):
            c = c - 65536;
        elif (c < 0):
            c = c + 65536;

        plaintext += chr(c);

    return plaintext;

### TEST ###

import random

text = "TeSt"
print("Text:",text)

key = random.randrange(65536);
print("Key:", key)

ctext = encrypt(text, key);
print("CipherText:", ctext);

ptext = decrypt(ctext, key);
print("PlainText:", ptext);


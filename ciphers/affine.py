# affine cipher

import math, random

## get key data from key string
def getkeys(key):
    keys = {};
    ## split key string into product and xor
    k1 = int(key.split(':')[0]);
    k2 = int(key.split(':')[1]);
    
    A1 = 0;
    A2 = 0;
    shift = 0;
    
    ## find first co-prime and shift from product and xor 
    for i in range(65536):
        if (math.gcd(65536, i) == 1) and ((k1 % i) == 0):
            for j in range(int(65536/2) - 1):
                if ((i * j) == k1) and ((i ^ j) == k2):
                    A1 = i;
                    shift = j;
                    break;
    
    ## find second co-prime
    for x in range(65536):
        if (((A1 * x) % 65536) == 1):
            A2 = x;
            break;
    
    keys = (A1, A2, shift);

    return keys;

## generate key data
def genKey():
    key = "";
    coprimes=[]

    ## find co-primes for 65536
    for i in range(65536):
        if (math.gcd(65536, i) == 1):
            coprimes.append(i);
    
    ## pick a random co-prime
    A1 = coprimes[(random.randrange(len(coprimes) - 1))];
    ## pick a random shift from half character space
    shift = random.randrange(int(65536/2) - 1);
    
    ## multiply shift and co-prime
    k1 = A1 * shift;
    ## xor shift and co-ptime
    k2 = A1 ^ shift;
    ## combine product and xor into a string
    key = str(k1) + ":" + str(k2);

    return key;

## encrypt text with key data C = ((A1 * c) + shift) % 65536
def encrypt(key, text):
    ctext = "";
    keys = getkeys(key);
    A1 = keys[0];
    A2 = keys[1];
    shift = keys[2];

    for c in range(len(text)):
        ctext += hex(((A1 * ord(text[c])) + shift) % 65536);

    return ctext;

## decrypt text with key data P = ((c - shift) * A2) % 65536
def decrypt(key, text):
    ptext = "";
    keys = getkeys(key);
    A1 = keys[0];
    A2 = keys[1];
    shift = keys[2];

    for c in range(1, len(text.split('0x'))):
        ptext += chr(int(((int(text.split('0x')[c], 16) - shift) * A2) % 65536))

    return ptext;

# test case

text = "test";

key = genKey();
print(key);

ctext = encrypt(key, text);
print(ctext);

ptext = decrypt(key, ctext);
print(ptext);


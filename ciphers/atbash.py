#Atbash cipher
#uses UTF-16 character set

def encrypt(text):
    ctext = "";

    for i in range(len(text)):
        c = (65535 - ord(text[i]));
        ctext += hex(c);

    return ctext;

def decrypt(text):
    ptext = "";
    
    for i in range(1, len(text.split('0x'))):
        c = (65535 - int(text.split('0x')[i], 16));
        ptext += chr(c);

    return ptext;

def test():
    text = "TeSt 1 2 3";
    ctext = encrypt(text);
    ptext = decrypt(ctext);

    print("Text:", text);
    print("Cipher Text:", ctext);
    print("Plain Text:", ptext);


test();


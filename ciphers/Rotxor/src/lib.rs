use std::char;
use std::env;
use std::error::Error;


pub struct Crypt {
    pub text: String,
    pub key: String,
    pub rotation: usize,
    //pub rounds: u32,
}

impl Crypt {
    pub fn new(mut args: std::env::Args) -> Result<Crypt, &'static str> {
        // skip first arg;
        args.next();

        // get 2nd arg; key
        let key = match args.next() {
            Some(arg) => arg,
            None => return Err("Pass Key not provided"),
        };

        // get 3rd arg; message text
        let text = match args.next() {
            Some(arg) => arg,
            None => return Err("Message text not provided"),
        };
        
       /* // get rounds
        let rounds = match args.next() {
            Some(arg) => arg,
            None => return Err("Cipher rounds not specified"),
        };*/
        
        // get rotation; length of key
        let rotation = key.chars().count();

        Ok(Crypt {
            text,
            key,
            rotation,
            //rounds,
        })
    }
}

pub fn encrypt(crypt: Crypt) -> Result<String, Box<dyn Error>> {
    let mut ctext = String::new();
    
    for (i, c) in crypt.text.char_indices() {
        let r = (c as u32) + ((crypt.rotation % 65535) as u32);
        let x = char::from_u32(r ^ (crypt.key.chars().nth(i % crypt.rotation).unwrap() as u32)).unwrap();

        ctext.push(x);

        // test
        //print!("{} ", x as u32);
    }

    let out = base64::encode_config(ctext, base64::URL_SAFE_NO_PAD);
    println!("Cipher text: {}", out);
    Ok(out)
}

pub fn decrypt(crypt: Crypt) -> Result<String, Box<dyn Error>> {
    let mut ptext = String::new();
    let ctext = String::from_utf8(base64::decode_config(crypt.text, base64::URL_SAFE_NO_PAD).unwrap()).unwrap();

    for (i, c) in ctext.char_indices() {
        let x = (c as u32) ^ (crypt.key.chars().nth(i % crypt.rotation).unwrap() as u32);
        let r = char::from_u32(x  - ((crypt.rotation % 65535) as u32)).unwrap();

        ptext.push(r);
    }
    
    println!("Plain text: {}", ptext);

    Ok(ptext)
}


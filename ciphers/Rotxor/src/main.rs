//use std::char;
use std::env;
use std::process;
use rotxor::Crypt;

/* encrypts and decrypts a string by shifting each char
 * by the lenght og the key.
 * the char is then xor'd by the char of the key at the same index
 * the cipher text is then base64 encoded.
 *
 * todo:
 * add rounds
 * add cli arg for encrypt/decrypt
 *
 * rotxor <key> <text>
 */

fn main() {
    let crypt = Crypt::new(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    if let Err(e) = rotxor::encrypt(crypt) {
        eprintln!("Error encrypting data {}", e);
        process::exit(1);
    }
}

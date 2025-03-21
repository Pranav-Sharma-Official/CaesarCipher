# CaesarCipher 

This Python script implements a simple Caesar cipher for encoding and decoding text.

## How it works

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet.

* **Encoding:** Shifts each letter in the input text by the specified shift amount.
* **Decoding:** Reverses the encoding process by shifting each letter back by the specified shift amount.
* **Wrapping:** The alphabet wraps around, so if a shift goes beyond 'z', it starts again from 'a'.
* **Non-alphabet characters:** Characters that are not in the alphabet (spaces, punctuation, numbers) are left unchanged.

## Usage

1.  **Run the script:** Execute the Python script.
2.  **Choose direction:** Enter "encode" to encrypt or "decode" to decrypt.
3.  **Enter message:** Type the message you want to encode or decode.
4.  **Enter shift number:** Provide the integer shift value.
5.  **View result:** The script will output the encoded or decoded message.

## Example

```bash
Type 'encode' to encrypt
, Type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here is the encoded result: mjqqt btwqi

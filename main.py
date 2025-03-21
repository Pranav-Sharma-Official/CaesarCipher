alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt\n, Type 'decode' to decrypt:\n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = (position + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter #Keep non alphabet characters
    print(f"Here is the encoded result: {cipher_text}")

def decode(original_text, shift_amount):
    plain_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = (position - shift_amount) % len(alphabet)
            plain_text += alphabet[shifted_position]
        else:
            plain_text += letter
    print(f"Here is the decoded result: {plain_text}")

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decode(original_text=text, shift_amount=shift)
else:
    print("Invalid direction.")

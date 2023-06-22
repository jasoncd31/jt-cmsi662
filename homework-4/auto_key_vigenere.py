def vigenere(plain_text, cipher_key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = plain_text.upper()
    key = cipher_key.upper()
    cipher_text = ""
    for index, c in enumerate(message):
        cipher_char = alphabet[(alphabet.index(message[index]) + alphabet.index(key[index]))%26]
        key += cipher_char
        cipher_text += cipher_char
    return (cipher_text, key[:len(cipher_text)])
   

plain_text = "TAKEACOPYOFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR"
key = "QUARK"
print(vigenere(plain_text, key))




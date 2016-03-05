#!/usr/bin/python3
import string
 
 
def encode(plaintext, key):
    ciphertext = ''
    alpha = string.ascii_lowercase
 
    for character in plaintext:
        if character.isalpha():
            new_character = alpha[((alpha.index(character.lower()) + key) % 26)]
            if character.islower():
                ciphertext += new_character.lower()
            else:
                ciphertext += new_character.upper()
        else:
            ciphertext += character
    return ciphertext
 
def decode(ciphertext, key):
    return encode(ciphertext, -key)
 
with open('zen_of_python.txt') as plaintext:
    for line in plaintext.readlines():
        print(encode(line, 7), end='')

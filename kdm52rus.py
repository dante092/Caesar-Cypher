

import string
import getopt
import sys
from collections import deque
 
 
def rotate_word(text, key):
 
    if not isinstance(text, str):
        return text
 
    if not len(text):
        return text
 
    len_ascii = len(string.ascii_letters)
    # using deque for fast append, also join is faster then string concatenation
    deq = deque()
    for letter in text:
        if letter not in string.ascii_letters:
            deq.append(letter)
            continue
        # calculating new letter via index manipulation
        index = string.ascii_letters.index(letter) + key
        if index >= len_ascii:
            index = len_ascii - 1 - index
        deq.append(string.ascii_letters[index])
    encrypted_string = "".join([letter for letter in deq])
    return encrypted_string
 
 
def caesar_cypher(args):
    try:
        opts, args = getopt.getopt(args, "", ["file=", "key="])
    except getopt.GetoptError:
        print("please use python file.py --file path_to_file --key number")
        sys.exit(2)
 
    for opt, arg in opts:
        if opt in ("--file",):
            file = arg
        elif opt in ("--key",):
            key = arg
 
    key = int(key)
    try:
        with open(file, 'r') as file:
            for text_line in file:
                encrypted = rotate_word(text_line, key)
                with open('encrypted.txt', mode='a', encoding='utf-8') as af:
                    af.write(encrypted)
    except FileNotFoundError as e:
        print("file do not exist")
        sys.exit()
 
 
if __name__ == "__main__":
    caesar_cypher(sys.argv[1:])

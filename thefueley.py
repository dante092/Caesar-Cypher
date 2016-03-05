import string
def rotate_word(str_plain, shift):
    """
   Will encrypt a string according to the Caesar Cipher
   
   :param str_plain: the plaintext string to encrypt
   shift: the number of chars to shift the string by
   :return:
   """
    shift %= 26
    print("Shift: " + str(shift))
   
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
   
    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]
   
    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper
   
    table = str_plain.maketrans(alphabet, shifted_alphabet)
   
    print(str_plain.translate(table))
   
if __name__ == '__main__':
    rotate_word("The Zen of Pytho text", 7)

def rotate_word(input_str, key):
    letters = list(input_str)
    for i in range(len(letters)):
        if not letters[i].isalpha(): # leave punctuation, number, space, etc alone
            continue
        if letters[i].isupper():
            letters[i] = chr((((ord(letters[i]) - 65) + key) % 26) + 65) # need to find a better way to wrap around here
        else:
            letters[i] = chr((((ord(letters[i]) - 97) + key) % 26) + 97)
    return "".join(letters)

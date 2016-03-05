test_word = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more oF those!"""

def rotate_word(coded_phrase, rotate_amt):
    new_phrase = '' 
    for x in coded_phrase:
        if x == " ": 
            y = " "
            new_phrase += y
        elif ord(x) + rotate_amt > 122: 
            y = chr(ord(x) + rotate_amt - 26)
            new_phrase += y
        elif ord(x) + rotate_amt > 90 and ord(x) + rotate_amt < 97: 
            y = chr(ord(x) + rotate_amt - 26)
            new_phrase += y
        elif ord(x) >= 65 and ord(x) <= 90 or ord(x) > 97 and ord(x) <= 122: 
            y = chr(ord(x) + rotate_amt)
            new_phrase += y
        else: 
            y = x
            new_phrase += y
    return new_phrase

print(rotate_word(test_word, 7))

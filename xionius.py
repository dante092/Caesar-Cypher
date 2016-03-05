def encode(some_text):
    s = ''
    for x in some_text:
        y = ord(x) + 7
        if 123 <= y <= 129 or 91 <= y <= 97:
            y = y - 26
        if y < 65  or y > 122:
            y = ord(x)
        s = s + chr(y)
    return s

def decode(other_text):
    s = ''
    for x in other_text:
        y = ord(x) - 7
        if 90 <= y <= 96 or 58 <= y <= 64:
            y = y + 26
        if y < 65  or y > 122:
            y = ord(x)
        s = s + chr(y)
    return s

orig_text = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!"""
encoded_text = encode(orig_text)
decoded_text = decode(encoded_text)
print("""

Encoded Text
""")
print(encoded_text)
print("""

Decoded Text
""")
print(decoded_text)


#!/usr/bin/python3
def encrypt(string, rotate):
    """
    Encrypt given input string with the caeser cypher.
    args:
        string (str):   string to encrypt.
        rotate (int):   number by whiche the characters are rotated.
    returns:
        str:            encrypted version of the input string.
    raises:
        TypeError:      if word is not a string or rotate not an int.
        ValueError:     if word is empty string or rotate is smaller than 1.
    """

    if not isinstance(string, str) or not isinstance(rotate, int):
        raise TypeError
    elif not string or rotate < 1:
        raise ValueError
    else:
        encrypted_string = ''
        for char in string:
            if not char.isalpha():
                encrypted_string += char
            else:
                char_code = ord(char)
                # check if rotated char code is bigger than char code of z
                if char_code + rotate > 122:
                    # if so, compute left rotations after z and start from a
                    char_code = 96 + (char_code + rotate - 122)
                # check if rotated char code is bigger than char code of Z but
                # smaller than char code of a
                elif char_code + rotate > 90 and char_code + rotate < 97:
                    # if so, compute left rotations after Z and start from A
                    char_code = 64 + (char_code + rotate - 90)
                else:
                    char_code += rotate
                encrypted_string += chr(char_code)

        return encrypted_string


def decrypt(string, rotate):
    """
    Decrypt given input string with the caeser cypher.
    args:
        string (str):   string to decrypt.
        rotate (int):   number by whiche the characters are rotated.
    returns:
        str:            decrypted version of the input string.
    raises:
        TypeError:      if word is not a string or rotate not an int.
        ValueError:     if word is empty string or rotate is smaller than 1.
    """

    if not isinstance(string, str) or not isinstance(rotate, int):
        raise TypeError
    elif not string or rotate < 1:
        raise ValueError
    else:
        decrypted_string = ''
        for char in string:
            if not char.isalpha():
                decrypted_string += char
            else:
                char_code = ord(char)
                # check if rotated char code is smaller than char code for a
                # but char code is bigger than char code for a - 1
                if char_code - rotate < 97 and char_code > 96:
                    # if true, than start over from z
                    char_code = 123 - (rotate - (char_code - 97))
                # check if rotated char code is smaller than A
                elif char_code - rotate < 65:
                    # if ture, than start over from Z
                    char_code = 91 - (rotate - (char_code - 65))
                else:
                    char_code -= rotate

                decrypted_string += chr(char_code)
        return decrypted_string

if __name__ == '__main__':
    zen = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

    zen_encrypt = "Ilhbapmbs pz ilaaly aohu bnsf. Lewspjpa pz ilaaly aohu ptwspjpa. Zptwsl pz ilaaly aohu jvtwsle. Jvtwsle pz ilaaly aohu jvtwspjhalk. Msha pz ilaaly aohu ulzalk. Zwhyzl pz ilaaly aohu kluzl. Ylhkhipspaf jvbuaz. Zwljphs jhzlz hylu'a zwljphs luvbno av iylhr aol ybslz. Hsaovbno wyhjapjhspaf ilhaz wbypaf. Lyyvyz zovbsk ulcly whzz zpsluasf. Buslzz lewspjpasf zpslujlk. Pu aol mhjl vm htipnbpaf, ylmbzl aol altwahapvu av nblzz. Aolyl zovbsk il vul-- huk wylmlyhisf vusf vul --vicpvbz dhf av kv pa. Hsaovbno aoha dhf thf uva il vicpvbz ha mpyza buslzz fvb'yl Kbajo. Uvd pz ilaaly aohu ulcly. Hsaovbno ulcly pz vmalu ilaaly aohu *ypnoa* uvd. Pm aol ptwsltluahapvu pz ohyk av lewshpu, pa'z h ihk pklh. Pm aol ptwsltluahapvu pz lhzf av lewshpu, pa thf il h nvvk pklh. Uhtlzwhjlz hyl vul ovurpun nylha pklh -- sla'z kv tvyl vm aovzl!"

    print("Starting assert-tests:")
    print("encrypting tests:")
    assert encrypt('abcd', 1) == 'bcde'
    print('Test 01: passed')
    assert encrypt('xyz', 2) == 'zab'
    print('Test 02: passed')
    assert encrypt('ABC', 2) == 'CDE'
    print('Test 03: passed')
    assert encrypt('Hallo', 3) == 'Kdoor'
    print('Test 04: passed')
    assert encrypt('XYZ', 2) == 'ZAB'
    print('Test 05: passed')
    assert encrypt(zen, 7) == zen_encrypt
    print("Test 06: passed")

    print("decrypting tests:")
    assert decrypt('bcde', 1) == 'abcd'
    print('Test 07: passed')
    assert decrypt('zab', 2) == 'xyz'
    print('Test 08: passed')
    assert decrypt('CDE', 2) == 'ABC'
    print('Test 09: passed')
    assert decrypt('Kdoor', 3) == 'Hallo'
    print('Test 10: passed')
    assert decrypt('ZAB', 2) == 'XYZ'
    print('Test 11: passed')
    assert decrypt(zen_encrypt, 7) == zen
    print("Test 12: passed")

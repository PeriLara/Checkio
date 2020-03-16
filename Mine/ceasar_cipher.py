"""
This mission is the part of the set. Another one - Caesar cipher decriptor.
Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"
"""
def to_encrypt(text, delta):  
    text2id = [(char, ord(char)) for char in text]
    encripted_text = []
    for char, index in text2id:
        if index == 32:
            encripted_text.append(" ")
        elif index + delta < 123 and index + delta > 96:
            encripted_text.append(chr(index + delta))
        elif index + delta > 122:
            encripted_text.append(chr(index + delta - 26))
        else:
            encripted_text.append(chr(index + delta + 26))
    return "".join(encripted_text)

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f", "def"
    assert to_encrypt("a b c", -3) == "x y z", "xyz"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")

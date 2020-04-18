"""Your task in this mission is to truncate a sentence to a length, that does not exceed a given number of characters.
If the given sentence already is short enough you don't have to do anything to it, but if it needs to be truncated the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.
The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.
Input: Two arguments:
one-line sentence as a string
max length of the truncated sentence as an int
Output: The shortened sentence plus the ellipsis (if required) as a one-line string.
Precondition:
line.startswith(' ') == False
0 < len(line) ≤ 79
0 < length ≤ 76
all(char in string.ascii_letters + ' ' for char in line)
"""
def cut_sentence(line, length):
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if length >= len(line):
        return line
    begin_word = 0
    sentence_cut = []
    for idx, token in enumerate(line.split()):
        begin_word += len(token) + 1
        sentence_cut.append(token)
        if begin_word > length:
            if line[length] == " ":
                return " ".join(sentence_cut) + "..."
            return " ".join(sentence_cut[:-1]) + "..."


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 10) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')



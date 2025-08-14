# remove_general_punc.py
# re.sub('\s{2,}', ' ', text)

import unicodedata

def remove_general_punc(s: str) -> str:
    """
    Removes characters from the Unicode General Punctuation block.
    Purpose: remove thin space characters from text by specifying codepoints

    Usage: pass string to function, such as an abstract from OpenAlex that has been reconstructed.

    Returns: a string with the General Punctuation Unicode block characters removed.
    """
    general_punctuation = set()
    for i in range(0x2000, 0x2070):
        general_punctuation.add(chr(i))

    return ''.join([char for char in s if char not in general_punctuation])

if __name__ == "__main__":
    print(remove_general_punc(s))

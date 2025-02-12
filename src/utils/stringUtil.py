import re

def isArabic(text): 
    return re.search(r'[\u0600-\u06FF]', text)

def reverseWordWiseForArabic(strr: str) -> str:
    words = []
    word = ''
    was_last_char_separator = False
    word_letter_pattern = re.compile(r'[A-Za-z0-9,]')

    for ch in strr:
        if word_letter_pattern.match(ch):
            if was_last_char_separator and word != "":
                words.append(word)
                word = ''
            word += ch
            was_last_char_separator = False
        else:
            if not was_last_char_separator and word != '':
                words.append(word)
                word = ''
            word += ch
            was_last_char_separator = True

    if word != '':
        words.append(word)

    reversed_words = []
    if not word_letter_pattern.match(words[0]):
        reversed_words.append(words.pop(0))  # don't reverse first space sequence

    if len(words) > 1 and not word_letter_pattern.match(words[-1]):
        # don't reverse last space sequence
        last_word = words.pop()
        reversed_words = reversed_words + list(reversed(words)) + [last_word]
    else:
        reversed_words = reversed_words + list(reversed(words))

    return ''.join(reversed_words)

def replace_substring(input_string: str, start: int, end: int, replacement: str) -> str:
    string_list = list(input_string)
    string_list[start:end] = replacement
    return ''.join(string_list)

def fixOrder(strr, cStr, ind):
    fixedNonArabicWord =  reverseWordWiseForArabic(cStr)
    return replace_substring(strr, ind - len(fixedNonArabicWord), ind, fixedNonArabicWord)

def fixArabic(strr: str) -> str:
    if (not isArabic(strr)):
        return strr
    
    cStr = ""
    for ind in range(len(strr)):
        ch = strr[ind]
        if (not isArabic(ch) and ( ch != " " or len(cStr))):
            cStr += ch
        else:
            if (cStr != ""):
                strr = fixOrder(strr, cStr, ind)
                cStr = ""
    strr = fixOrder(strr, cStr, len(strr)) if cStr != "" else strr
    return strr


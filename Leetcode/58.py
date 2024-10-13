def lengthOfLastWord(s):
    ptr = len(s) - 1
    word_length = 0

    if len(s) == 1:
        return 1
    
    while ptr >= 0:
        if s[ptr] != ' ':
            word_length += 1
            ptr -= 1
            while s[ptr] != ' ' and ptr >= 0:
                word_length += 1
                ptr -= 1
            return word_length
        else:
            ptr -= 1

    return word_length

print(lengthOfLastWord('boy'))
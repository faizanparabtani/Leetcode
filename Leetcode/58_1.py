def lengthOfLastWord(s):
    word_length = 0
    word_encountered = False
    for i in s[::-1]:
        if i != " ":
            word_length += 1
            word_encountered = True
        else:
            if word_encountered:
                return word_length
    return word_length

            



s = "Hello Worlds sas s        sa     wssss aaaa a aa                     "
print(lengthOfLastWord(s))
            
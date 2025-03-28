def wordPattern(pattern, s):
    words, w_to_p = s.split(' '), dict()

    if len(pattern) != len(words): return False
    if len(set(pattern)) != len(set(words)): return False # for the case w = ['dog', 'cat'] and p = 'aa'

    for i in range(len(words)):
        if words[i] not in w_to_p: 
            w_to_p[words[i]] = pattern[i]
        elif w_to_p[words[i]] != pattern[i]: 
            return False

    return True

pattern = "abba"
s = "dog dog dog dog"

print(wordPattern(pattern, s))
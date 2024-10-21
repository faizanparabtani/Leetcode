def wordPattern(pattern, s):
    s_list = s.split(' ')
    if len(pattern) != len(s_list):
        return False

    for index, value in enumerate(pattern):
        try:
            index_exists = s_list[index]
        except:
            return False
    
    return True

pattern = "abb"
s = "dog cat cat dog"

print(wordPattern(pattern, s))
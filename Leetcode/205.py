from collections import Counter

def isIsomorphic(self, s, t):
    s_counter = Counter(s)
    t_counter = Counter(t)
    
    if len(s_counter) != len(t_counter):
        return "false"

    index = 0
    while len(t_counter) > 0:
        letter_count_s = s_counter[index]
        
        
def isSubsequence(s, t):
    s_ptr = t_ptr = 0
    while t_ptr < len(t):
        if s_ptr < len(s):
            print(s[s_ptr], t[t_ptr])
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1
        else:
            return s_ptr == len(s)
    return s_ptr == len(s)



print(isSubsequence('axc', 'ahbdce'))
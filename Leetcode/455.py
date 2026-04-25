def findContentChildren(g, s):
    no_of_students = len(g)
    if no_of_students == 0:
        return 0

    s.sort()
    g.sort()

    s_ptr = 0
    g_ptr = 0
    satisfied_student = 0
    while g_ptr < no_of_students and s_ptr < len(s):
        if s[s_ptr] >= g[g_ptr]:
            satisfied_student += 1
            g_ptr += 1
        s_ptr += 1

    return satisfied_student


g = [1, 2, 3]
s = [1, 1]

print(findContentChildren(g, s))

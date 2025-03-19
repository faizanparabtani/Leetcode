# Using Sorted - O(nlogn)
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s_sorted = sorted(s)
    t_sorted = sorted(t)
    print(s_sorted, t_sorted)

    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:
            return False
    return True


# Using Hashmaps O(n)
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    counter = {}

    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1

    return True

s = "aba"
t = "abc"
# s = "anagram"
# t = "nagaram"

ans = isAnagram(s, t)
print(ans)

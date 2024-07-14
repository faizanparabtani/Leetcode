# def isAnagram(s, t):
#     hashmap_one = {}
#     hashmap_two = {}
#     for i in s:
#         if i in hashmap_one:
#             hashmap_one[i] += 1
#         else:
#             hashmap_one[i] = 1
    
#     for i in t:
#         if i in hashmap_two:
#             hashmap_two[i] += 1
#         else:
#             hashmap_two[i] = 1

#     same = {k: hashmap_one[k] for k in hashmap_one if k in hashmap_two and hashmap_one[k] == hashmap_two[k]}
#     if len(same) != len(hashmap_one) or len(same) != len(hashmap_two):
#         return False
    
#     return True


# def isAnagram(s, t):    
#     if len(s) != len(t):
#             return False
#     freq = [0] * 26
#     for i in range(len(s)):
#         freq[ord(s[i]) - ord('a')] += 1
#         freq[ord(t[i]) - ord('a')] -= 1

#     for i in range(len(freq)):
#         if freq[i] != 0:
#             return False

#         return True

    
# def isAnagram(s, t):
#     # In case of different length of thpse two strings...
#     if len(s) != len(t):
#         return False
#     for i in set(s):
#         print(i, s.count(i), t.count(i))
#         # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
#         # If they are different, return false...
#         if s.count(i) != t.count(i):
#             return False
#     return True     # Otherwise, return true...

# s = "aba"
# t = "abc"

# ans = isAnagram(s, t)
# print(ans)

for i in xrange(5):
    print(i)

# print(set(s))
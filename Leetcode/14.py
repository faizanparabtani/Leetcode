# My solution - O(m * n)
# def longestCommonPrefix(strs):
#     # My solution
#     strslen = len(strs)
#     prefix = strs[0]
#     prev = 0
#
#     if strslen == 0:
#         return ""
#     elif strslen == 1:
#         return strs[0]
#
#     for i in range(1, strslen):
#         j = 0
#         while j < min(len(strs[i]), len(prefix)):
#             if strs[i][j] == prefix[j]:
#                 print(strs[i][j], prefix[j])
#
#                 j += 1
#             else:
#                 break
#         prefix = strs[i][0:j]
#         prev += 1
#     return prefix


# Better solution O(nlogn)
def longestCommonPrefix(v):
    ans = ""
    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

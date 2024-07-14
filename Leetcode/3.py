# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         pointer, length_longest = 0, 0
#         my_map = {}
#         lenght_list = []

#         while(pointer < len(s)):
#             if s[pointer] in my_map:
#                 lenght_list.append(length_longest)
#                 my_map = {}
#                 my_map[s[pointer]] = 1
#                 length_longest = 1
#             elif s[pointer] not in my_map:
#                 my_map[s[pointer]] = 1
#                 length_longest += 1
#             pointer += 1
            
#         lenght_list.append(length_longest)
#         return max(lenght_list)


class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res
        


test = "dvdf"
solutionobject = Solution()
result = solutionobject.lengthOfLongestSubstring(test)
print(result)
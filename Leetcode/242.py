class Solution(object):
    def isAnagram(self, s, t):

        s_len, t_len = len(s), len(t)
        s_pointer = 0
        t_pointer = t_len - 1

        if s_len != t_len:
            return "false"
        
        for i in range(s_len):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer -= 1
            else:
                return "false"
        
        return "true"


s = Solution()

print(s.isAnagram('rat', 'car'))
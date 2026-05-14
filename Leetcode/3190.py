class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for i in nums:
            if i % 3 == 1 or i % 3 == 2:
                output += 1

        return output
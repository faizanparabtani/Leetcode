class Solution(object):
    def twoSum(self, nums, target):
        myMap = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result not in myMap:
                myMap[nums[i]] = i
            elif result in myMap:
                return [myMap[result], i]
            
        
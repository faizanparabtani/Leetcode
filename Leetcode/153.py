def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    minimum = nums[0]
    while l < r:
        mid = (l+r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
        
    return nums[l]
        


nums = [3,4,5,1,2]
print(findMin(nums))
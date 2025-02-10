 def containsNearbyDuplicate(nums, k):
    if len(nums) < 2:
            return False 

    numbers_visted = {}

    for i in range(len(nums)):
        if nums[i] in numbers_visted:
            numbers_visted[nums[i]] = i
            print(numbers_visted)
            abs_value = abs(numbers_visted[nums[i] - i])
            if abs_value <= k:
                return True
        continue
    return False


nums = [1,2,3,1,2,3]
print(containsNearbyDuplicate(nums))



def containsNearbyDuplicate(nums, k):
    if len(nums) < 2:
        return False 

    numbers_visted = {}

    for i in range(len(nums)):
        if nums[i] not in numbers_visted:
            numbers_visted[nums[i]] = i
            continue
        abs_value = abs(numbers_visted[nums[i]] - i)
        if abs_value <= k:
            return True
        continue
        
    return False


def containsNearbyDuplicate(nums, k):
    seen = set()

    for idx, val in enumerate(nums):
        if val in seen:
            return True
        seen.add(val)

        if len(seen) > k:
            seen.remove(nums[idx-k])

    return False


nums = [1,0,1,1]
print(containsNearbyDuplicate(nums, 1))



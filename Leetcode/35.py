def searchInsert(nums, target):
	left, right = 0, len(nums) - 1

	if len(nums) == 1:
		if nums[0] < target:
			return 1
		else:
			return 0
      
	while left != right:
		mid = left + right // 2
		if nums[mid] == target:
			return mid
		elif target > nums[mid]:
			left = mid + 1
		elif target < nums[mid]:
			right = mid - 1
    
	return left

nums = [1,3,5,6]
target = 2

print(searchInsert(nums, target))
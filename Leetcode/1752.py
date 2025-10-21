def check(nums):
	count = 0
	for i in range(1, len(nums)):
		if nums[i-1] > nums[i]:
			count += 1

	if nums[-1] > nums[0]:
		count += 1

	return count <= 1


nums = [3,4,5,1,7]
print(check(nums))

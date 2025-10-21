def secondLargestElement(nums):
	largest = nums[0]
	second_largest = None
	if len(nums) == 1:
		return -1
	for i in range(1, len(nums)):
		if nums[i] > largest:
			second_largest = largest
			largest = nums[i]
		elif largest - nums[i] == 1:
			second_largest = nums[i]
		print(largest, second_largest)
		
	if second_largest:
		return second_largest
	return -1



nums =  [10, 10, 10, 10, 10]
print(secondLargestElement(nums))
def rotate(nums, k):
	nums_len = len(nums)
	rotation_no = k

	if k > len(nums):
		rotation_no = k % nums_len

	left = 0
	right = rotation_no

	while right < nums_len:
		print(left, right, rotation_no)
		if right < nums_len:
			temp = nums[right]
			nums[right] = nums[left]
			nums[left] = temp

			left += 1
			right += 1

	right = rotation_no - 1 
	while left <= right:
		print(left, right, rotation_no)
		temp = nums[right]
		nums[right] = nums[left]
		nums[left] = temp

		left += 1
		right -= 1

	return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))
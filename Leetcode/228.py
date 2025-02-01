def summaryRanges(nums):
	if len(nums) == 0:
		return

	ans_list = []
	i = 0
	jump = 1
	while i+jump < len(nums):
		print(f"nums[i]: {nums[i]}, jump:{jump}, nums[i+jump]:{nums[i+jump]}")
		if nums[i+jump] == nums[i] + 1:
			jump += 1
		else:
			if jump > 1:
				ans_list.append(f"{nums[i]}->{nums[i+jump-1]}")
			else:
				ans_list.append(f"{nums[i]}")
			i += jump
			jump = 1

	return ans_list
		


nums = [0,1,2,4,5,7]
result = summaryRanges(nums)
print(result)
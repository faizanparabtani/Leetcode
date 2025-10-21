# def findMaxConsecutiveOnes(nums):
	current_max = 0
	overall_max = 0
	for i in range(len(nums)):
		if nums[i] == 1:
			current_max += 1
		else:
			overall_max = max(overall_max, current_max)
			current_max = 0

		overall_max = max(overall_max,current_max)

	return overall_max


nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))
def maximumTripletValue(nums):
	i = 0
	j = 1
	k = 2

	max_value = 0

	while j < len(nums)-1:
		k = j+1
		print(i, j, k)
		if nums[i] > nums[j]:
			subtraction_value = nums[i] - nums[j]
			while k < len(nums):
				current_value = subtraction_value * nums[k]
				max_value = max(max_value, current_value)
				k+=1
		i+=1
		j+=1

	return max_value


nums = [12,6,1,2,7]
print(maximumTripletValue(nums))
def moveZeroes(nums):
	left = 0
	right = 0

	while right < len(nums):
		if nums[right] != 0:
			nums[left], nums[right] = nums[right], nums[left]
			left += 1
		
		right += 1


# def moveZeroes(nums):
# 	left, right = 0, 0  # Both pointers start at the beginning

#     while right < len(nums):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1  # Move left only when we swap a nonzero element
        
#         right += 1  # Always move right


nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
def minSubArrayLen(target, nums):
	l = 0
	total = 0
	res = float('inf')

	for r in range(len(nums)):
		total += nums[r]

		while total >= target:
			res = min(res, r-l+1)

			total -= nums[l]
			l += 1

	if res == float('inf'):
		return 0
	
	return res

target = 11
nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(target, nums))
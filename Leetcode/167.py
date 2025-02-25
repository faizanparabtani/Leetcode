def twoSum(numbers, target):
	left = 0
	right = len(numbers) - 1

	while left < right:
		current_sum = numbers[left] + numbers[right]
		if  current_sum == target:
			return [left, right]
		elif current_sum > target:
			right -= 1
		else:
			left += 1


numbers = [-1,0]
target = -1

answer = twoSum(numbers, target)
print(answer)
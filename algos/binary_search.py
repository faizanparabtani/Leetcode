# Iterative
def binary_search(nums, k):
	left = 0
	right = len(nums) - 1
	mid = len(nums) // 2

	while left <= right:
		mid = (left + right) // 2
		if nums[mid] > k:
			right = mid - 1
		elif nums[mid] < k:
			left = mid + 1
		elif nums[mid] == k:
			return mid

	return "Couldnt locate element"


"""
Recursive

"""



nums = [1, 2, 4, 5, 7, 10, 1000]
k = 1000
result = binary_search(nums, k)
print(result)
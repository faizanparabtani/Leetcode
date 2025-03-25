def minimumAbsDifference(arr):
	arr.sort() #O(nlogn)

	min_diff = float('inf')

	for i in range(1, len(arr)):
		min_diff = min(min_diff, arr[i] - arr[i-1])


	res_list = []
	for i in range(1, len(arr)):
		if arr[i] - arr[i-1] == min_diff:
			res_list.append([arr[i-1], arr[i]])

	return res_list


arr = [4,2,1,3]
print(minimumAbsDifference(arr))

def closestToZero(lis):
	# Checking if List is Empty and returning 0 if it is
	if len(lis) == 0:
		return 0

	# Setting result as first element
	res = abs(lis[0])

	for i in range(1, len(lis)):
		if abs(lis[i]) < res:
			res = lis[i]
		elif abs(lis[i]) == abs(res):
			if lis[i] > res:
				res = lis[i]
	return res



lis = [-2, -1, 1, 2, 5, 10]

print(closestToZero(lis))
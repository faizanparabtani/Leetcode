def longestCommonPrefix(strs):
	strslen = len(strs)
	dim = len(max(strs))
	lettermatrix = [[0 for _ in range(dim)]]*strslen
	for i, j in enumerate(strs):
		for ind, val in enumerate(j):
			# lettermatrix[i][ind] = val
			print(val)

	for i, val in enumerate(lettermatrix):
		print(val)
		# for j in enumerate(lettermatrix):
			# print(lettermatrix[i][j]) 
			


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

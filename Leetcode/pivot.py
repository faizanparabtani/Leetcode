def pivotIndex(nums):
	S = sum(nums)
	leftsum = 0
	for ind, val in enumerate(nums):
		if leftsum == (S - leftsum - val):
			return ind
		leftsum+=x
	return -1
	# asc = 0
	# numslen = len(nums)
	# desc = numslen - 1
	# ascsum, descsum = 0, 0

	# while asc <= desc:
	# 	if ascsum != descsum or asc != desc:
	# 		print(asc, desc)
	# 		print(f'Ascsum: {ascsum}, Descsum: {descsum}')
	# 		if ascsum > descsum:
	# 			descsum += nums[desc]
	# 			desc-=1
	# 		elif ascsum < descsum:
	# 			ascsum += nums[asc]
	# 			asc+=1
	# 		elif ascsum == descsum:
	# 			descsum += nums[desc]
	# 			ascsum += nums[asc]
	# 			asc+=1
	# 			desc-=1
	# 	elif ascsum == descsum:
	# 		return asc
	# 	elif ascsum == 0:
	# 		return numslen-1
	# 	elif descsum == 0:
	# 		return 0
	# 	else:
	# 		return -1
		



# def pivotIndex(nums):
# 	sumarr = []
# 	elesum = 0
# 	for i in nums:
# 		sumarr.append(elesum+i)



nums = [1,7,3,6,5,6]
nums = [8,1,2,2,2,2]
nums = [1,2,3]
nums = [2,1,-1]
print(pivotIndex(nums))
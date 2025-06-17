def longestCommonPrefix(strs):
	# Solution
	pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref


	# MY ATTEMPT
	# max_prefix = len(strs[0])
	# if len(strs) == 1:
	# 	return strs[0]		

	# for i in range(1, len(strs)):
	# 	if len(strs[i]) < max_prefix:
	# 		max_prefix = len(strs[i])
	# 		if max_prefix == 0:
	# 			return 0

	# 	actual_length = 0
	# 	for j in range(max_prefix):
	# 		print(strs[i-1][j], strs[i][j], actual_length)
	# 		if strs[i-1][j] == strs[i][j]:
	# 			actual_length += 1

	# 	max_prefix = actual_length
	# print(max_prefix)
	# if max_prefix == 1:
	# 	return strs[0][0]
	# else:
	# 	return strs[0][:max_prefix]

		


# strs = ["flower","flow","flight"]
strs = ["car", "cir"]

print(longestCommonPrefix(strs))
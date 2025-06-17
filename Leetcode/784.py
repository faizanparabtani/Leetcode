def letterCasePermutation(s):
	output = [""]
	for c in s:
		tmp=[]
		if c.isalpha():
			for o in output:
				tmp.append(o+c.upper())
				tmp.append(o+c.lower())
		else:
			for o in output:
				tmp.append(o+c)

		output=tmp
	return output


print(letterCasePermutation("a1b2"))
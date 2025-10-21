def print_star_pattern(n):
	letter_A = 65
	for i in range(1, n+1):
		for j in range(1, i+1):
			print(f"{chr(letter_A)}", end="")
		letter_A+=1
		print("")
	# for i in range(1, n+1):
	# 	for j in range(1, i+1):
	# 		print(f"{j}", end="")
	# 	for j in range((n-i)*2):
	# 		print(f" ", end="")
	# 	for j in range(i, 0, -1):
	# 		print(f"{j}", end="")
	# 	print("")


print_star_pattern(5)

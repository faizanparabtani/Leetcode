def isHappy(n):
	numbers_visited = set()
	sum_of_digits = 0

	def get_next_number(n):
		output = 0

		while n:
			digit = n % 10
			output += digit**2
			n = n // 10

		return output

	while n not in numbers_visted:
		numbers_visited.add(n)
		n = get_next_number(n)
		if n == 1:
			return True
		
	return False

n = 19
isHappy(n)
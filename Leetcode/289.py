def gameOfLife(board):
	board_copy = list(board)
	for i in range(len(board)):
		for j in range(len(board[i])):
			neighbours_sum = 0
			# Right
			if j+1 < len(board[i]): 
				right = board[i][j+1]
				neighbours_sum += right
				print(f'right: {right}')
			# Left
			if j-1 >= 0:
				left = board[i][j-1]
				neighbours_sum += left
				print(f'left: {left}')
			# Top
			if i-1 >= 0:
				top = board[i-1][j]
				neighbours_sum += top
				print(f'top: {top}')
			# Bottom
			if i+1 < len(board):
				bottom = board[i+1][j]
				neighbours_sum += bottom
				print(f'bottom: {bottom}')
			# Diag1
			if i+1 < len(board) and j-1 >= 0:
				diag1 = board[i+1][j-1]
				neighbours_sum += diag1
				print(f'diag1: {diag1}')
			# Diag2
			if i+1 < len(board) and j+1 < len(board[i]):
				diag2 = board[i+1][j+1]
				neighbours_sum += diag2
				print(f'diag2: {diag2}')
			# Diag3
			if i-1 >= 0 and j+1 < len(board[i]):
				diag3 = board[i-1][j+1]
				neighbours_sum += diag3
				print(f'diag3: {diag3}')
			# Diag4
			if i-1 >= 0 and j-1 >= 0:
				diag4 = board[i-1][j-1]
				neighbours_sum += diag4
				print(f'diag4: {diag4}')

			print(f'element: {board[i][j]}, neighbours_sum: {neighbours_sum}')
			# Death scenarios
			if neighbours_sum < 2:
				board_copy[i][j] = 0
			elif neighbours_sum > 3:
				board_copy[i][j] = 0
			# Life scenarios
			elif neighbours_sum == 3:
				board_copy[i][j] = 1
			elif 2 <= neighbours_sum <= 3:
				board_copy[i][j] = 1

	return board_copy





board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# board = [[1,1],[1,0]]
ans = gameOfLife(board)
print(ans)
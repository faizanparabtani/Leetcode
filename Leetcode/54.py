def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    max_row = len(matrix)
    max_col = len(matrix[0])

    spiral_order_list = []

    while max_row > len(matrix) - 2:
        while max_col > len(matrix[0]) - 2:
            spiral_order_list.append(matrix[max_row][max_col])
            max_col += 1
            max_row += 1


matrix = [[1,2,3],[4,5,6],[7,8,9]]
answer = spiralOrder(matrix)
print(answer)

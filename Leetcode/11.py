def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """

    i = 0
    j = 1
    area = 0
    max_area = 0
    while j < len(height):
        if height[i] < height[j]:
            max_area = max((height[i] * j-i), max_area)
            i+= 1
        else:
            max_area = max((height[j] * j-i), max_area)
            j+= 1

            


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
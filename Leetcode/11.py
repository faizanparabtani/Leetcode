def maxArea(height):
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

    return max_area


def maxArea(height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

            


height = [1,8,6,2,5,4,8,3,7]
result = maxArea(height)
print(result)
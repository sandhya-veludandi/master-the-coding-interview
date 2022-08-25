def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxArea = 0
    for i in range(len(height)-1):
        curr_height = height[i]
        j = i + 1
        while j in range(len(height)): 
            other_height = height[j]
            length = min(curr_height, other_height)
            width = j - i
            newArea = length*width
            maxArea = max(maxArea, newArea)
            j += 1
    return maxArea
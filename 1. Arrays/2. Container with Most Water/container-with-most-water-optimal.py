def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxArea = 0
    a_index = 0
    b_index = len(height)-1
    while a_index != b_index: 
        a = height[a_index]
        b = height[b_index]
        newArea = min(a, b)*(b_index-a_index)
        maxArea = max(maxArea, newArea)
        if a < b: 
            a_index += 1
        else:
            b_index -= 1
    return maxArea
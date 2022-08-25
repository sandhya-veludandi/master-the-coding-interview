def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    total_water_amt = 0
    p = 0
    while p < len(height): 
        #search for the max to the left of p
        maxL = p
        maxR = p
        i = p-1
        while i >= 0: 
            if (height[i] > height[maxL]): 
                maxL = i
            i -= 1
        j = p+1
        while j < len(height): 
            if(height[j] > height[maxR]): 
                maxR = j
            j += 1
                
        water_amt = min(height[maxL], height[maxR]) - height[p]
        if water_amt > 0: 
            total_water_amt += water_amt
        p += 1
    return total_water_amt
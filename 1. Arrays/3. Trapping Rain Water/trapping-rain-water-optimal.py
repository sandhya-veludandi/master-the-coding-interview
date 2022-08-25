def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    total_water_amt = 0
    pL = 0
    pR = len(height)-1
    maxL = 0
    maxR = len(height)-1
    while(pL != pR): 
        #where the left side has the shortest height
        if height[pL] <= height[pR]: 
            #calculate water amt if true
            if height[maxL] > height[pL]: 
                total_water_amt += height[maxL] - height[pL]
            #update max
            else: 
                maxL = pL
            pL += 1
        #where the right side has the shortest height
        else: 
            #calculate water amt if true
            if height[maxR] > height[pR]: 
                total_water_amt += height[maxR] - height[pR]
            #update max
            else: 
                maxR = pR
            pR -= 1
    return total_water_amt
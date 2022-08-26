def binarySearch(self, nums, left, right, target, ranges, prevMid):
    if nums == []: 
        return [-1, -1]
    initialPos = self.binarySearch(nums, 0, len(nums)-1, target); 
    if initialPos == -1: return [-1, -1]; 
    lowPos = initialPos
    highPos = initialPos
    tempLeft = None
    tempRight = None
    while lowPos != -1:
        #save the last time target was found
        tempLeft = lowPos
        lowPos = self.binarySearch(nums, 0, lowPos - 1, target)

    while highPos != -1: 
        tempRight = highPos
        highPos = self.binarySearch(nums, highPos + 1, len(nums)-1, target)
    
    return [tempLeft, tempRight]
def binarySearch(self, nums, left, right, target, ranges, prevMid):
    if left <= right: 
        mid = (right+left)/2
        if target == nums[mid]: 
            if mid < ranges[0] or ranges[0] == -1: 
                ranges[0] = mid
            if ranges[1] < mid: 
                ranges[1] = mid
            
            if prevMid != -1: 
                #right
                if prevMid < mid: 
                    return self.binarySearch(nums, mid+1, right, target, ranges, mid)
                else: 
                    return self.binarySearch(nums, left, mid-1, target, ranges, mid)
            else: 
                self.binarySearch(nums, left, mid-1, target, ranges, mid)
                self.binarySearch(nums, mid+1, right, target, ranges, mid)
                
        elif target < nums[mid]: 
            return self.binarySearch(nums, left, mid-1, target, ranges, prevMid)
        else: 
            return self.binarySearch(nums, mid+1, right, target, ranges, prevMid)
    return ranges
def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    prevMid = -1
    ranges = [-1, -1]
    
    if nums == []: 
        return ranges
    if len(nums) == 1: 
        if nums[0] == target: 
            return [0, 0]
        else: 
            ranges
    if target < nums[0] or nums[-1] < target: 
        return ranges
    
    return self.binarySearch(nums, 0, len(nums)-1,target, ranges, prevMid)
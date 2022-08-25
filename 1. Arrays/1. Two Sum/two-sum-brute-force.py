def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    results = []
    #Iterate thru all numbers except the last one in the outer for loop
    for i in range(len(nums)-1): 
        #Pointer 1
        num = nums[i]
        #Based on pointer1's number, we're trying to find the number that will
        #add up to the target: numToFind = target - pointer1
        numToFind = target - num
        #Pointer 2
        j = i + 1
        #Iterate through the rest of the numbers
        while j in range(len(nums)): 
            if nums[j] == numToFind: 
                results.append(i)
                results.append(j)
                return results
            j += 1
    return None
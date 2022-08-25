def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #Hashmap solution
    #Hashmap will contain previously calculated ntfs
    hashmap = {}
    for i in range(len(nums)):
        curr_num = nums[i]
        numToFind = target - curr_num
        #if curr_num in hashmap, return the indices
        if curr_num in hashmap: 
            return [i, hashmap[curr_num]]
        #otherwise, add the new ntf to the hashmap
        hashmap[numToFind] = i
    return None
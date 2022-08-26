def partition(self, arr, low, high):
    #holds the place of where the pivot should be
    i = low
    #scans and compares #s against pivot
    j = low
    #pivot is rightmost element
    pivot = arr[high]
    while j < high: 
        if arr[j] < arr[high]:
            if i != j: 
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else: 
            j += 1
    arr[i], arr[high] = pivot, arr[i]
    return i
    
def quickSelect(self, arr, low, high, k): 
    if low < high: 
        partition = self.partition(arr, low, high)
        if k == partition: 
            return arr[k]
        elif k > partition: 
            return self.quickSelect(arr, partition+1, high, k)
        else: 
            return self.quickSelect(arr, low, partition-1, k)
    return arr[k]
    
        
def findKthLargest(self, arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    indexToFind = len(arr)-k
    return self.quickSelect(arr, 0, len(arr)-1, indexToFind)
# Binary Search
Time: O(logn) → spend time searching thru half of array
## Iterative
Space: O(1) 
```
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums)-1
    while left <= right: 
        mid = (left+right)/2
        if target == nums[mid]: 
            return mid
        elif target < nums[mid]: 
            right = mid -1
        else: 
            left = mid + 1
    return -1
```
## Recursive
Space: O(n)
```
def binarySearch(self, nums, left, right, target):
    if left <= right: 
        mid = (right+left)/2
        if target == nums[mid]: 
            return mid
        elif target < nums[mid]: 
            return self.binarySearch(nums, left, mid-1, target)
        else: 
            return self.binarySearch(nums, mid+1, right, target)
    return -1

def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return self.binarySearch(nums, 0, len(nums)-1, target)
```

# Bubble Sort
## Sort: 6 5 3 1 8 7 2 4
```
Logic: sliding window between 2 elements (swap if curr < prev) 
while list not sorted:
  if prev element < curr element:
    move sliding window
  else:
    swap prev and curr elements
```
## Example: 
1 iteration thru whole array:
``` 
6 5 3 1 8 7 2 4 (swap 6 and 5)
5 6 3 1 8 7 2 4 (swap 6 and 3)
5 3 6 1 8 7 2 4 (swap 6 and 1)
5 3 1 6 8 7 2 4 (keep 6 and 8) 
5 3 1 6 8 7 2 4 (swap 8 and 7)
5 3 1 6 7 8 2 4 (swap 8 and 2)
5 3 1 6 7 2 8 4 (swap 8 and 4)
5 3 1 6 7 2 4 | 8 (8 is correctly sorted)
```
2 iter: 
```
...
3 1 5 6 2 4 | 7 8 (7 is correctly sorted)
...
8 iter: 
| 1 2 3 4 5 6 7 8 (1 is correctly sorted)
```
Patterns: The highest unsorted number (highest number not at end of array) will be continuously swapped until it reaches the end. 
## Time + Space Complexity:
* Time: O(n^2)
* Space: O(1)
## Best Case: 
O(n): continuously comparing between 2 elements
Code
```Python
def bubbleSort(arr):
    """
    :type arr: list
    :rtype: list
    """
    bubble = len(arr)
    for i in range(bubble-1):
        for j in range(0, bubble-1):
            # j and j + 1
            if arr[j] > arr[j+1]:
                 # swap them
                 temp = arr[j]
                 arr[j] = arr[j+1]
                 arr[j+1] = temp
        bubble -= 1
    return arr
```
# Insertion Sort
## Sort: 6 5 3 1 8 7 2 4
```
Logic: 
* numbers are divided into sorted (left) and unsorted (right) parts. 
* first item in list is always considered sorted
* take the first element in the unordeded part and move it from right to left 
```
1 iteration thru whole array: 
```
6 | 5 3 1 8 7 2 4 (swap 5 and 6)
```
2 iter:
``` 
5 6 | 3 1 8 7 2 4 (swap 3 and 6, swap 3 and 5)
...
3 5 6 | 1 8 7 2 4
``` 
8 iter: 
```
1 2 3 4 5 6 7 | 8
1 2 3 4 5 6 7 8 | 
```
Patterns: as move down array, the extra included item is sorted among the already sorted items
## Time + Space Complexity:
* Time: O(n^2)
* Space: O(1)
## Best Case: 
List is almost or is sorted and small data sets: O(n)
## Code
```Python
def insertionSort(arr):
    """
    :type arr: list
    :rtype: list
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            # if previous element is larger than current: like 3 2
            if arr[j] < arr[j-1]:
                # swap
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            j -= 1
            

    return arr
```
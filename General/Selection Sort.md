# Selection Sort
## Sort: 8 5 2 6 9 3 1 4 0 7
```
Logic: 2 pointers
* first ptr tracks the min so far and compares it with second ptr (min)
* second ptr scans the rest of the list for the smallest number (scanner). 
* if scanner < min:
    min = scanner. 
* at end of the list, swap minimum number with the current position to be sorted. 
* at each iteration, next min # is placed in the right position.
```
1 iteration thru whole array: 
```
8 5 2 6 9 3 1 4 0 7 (0 and 8 swap)
```
2 iter: 
```
0 | 5 2 6 9 3 1 4 8 7 (1 and 5 swap)
```
8 iter: 
```
1 2 3 4 5 6 7 | 8
```
Patterns: At each iteration, the min # is searched and swapped with the next unsorted index

## Time + Space Complexity:
* Time: O(n^2)
* Space: O(1)

## Code
```Python
def selectionSort(arr):
  """
  :type arr: list
  :rtype: list
  """
  for i in range(len(arr)-1):
      comparison = arr[i]
      temp = arr[i]
      index = i + 1
      for j in range(i + 1, len(arr)):
          scanner = arr[j]
          if scanner < comparison:
              comparison = scanner
              index = j
      arr[i] = comparison
      arr[index] = temp

  return arr
```
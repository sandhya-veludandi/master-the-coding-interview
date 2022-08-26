# Hoarse's QuickSelect Algorithm
Used to find the kth smallest element in unordered list. 
```
Given: [5, 3, 1, 6, 4, 2] and k = 4
Final Answer with Quick Sort: [1, 2, 3, 4, 5, 6] → 4
```
Logic: since we don’t care about sorting all elements, only sort on one half of the branch where we know k will be

## kth smallest
[[1], 2, [5, 6, 4, 3]]
partition = 2
k = 4, sort only on the right branch 
```
if k < partition: 
  sort on left branch
elif k > partition:
  sort on right branch
else:
  return arr[partition]
```
## kth largest
Logic: simply change the k value so that it uses the same logic as kth smallest
`k = len(arr) - k`

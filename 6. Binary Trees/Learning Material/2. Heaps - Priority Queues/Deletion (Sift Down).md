# Deletion (Sift Down)
## Conceptual
### Max Heap 
* Removal deletion, retrieval, return root value (greatest value)
* Restructure heap so max value at root and so tree is complete binary tree
* Take last node and place it in the root node and sift value down
## Example
```
        75
    50       25
  45  35   10  15
20 40
```
* save 75 into variable, then get rid of 40 
* swap 75 and 40 variable 
* set 45’s right child to null
```
        40
    50       25
  45  35   10  15
20
```
* max(left child, right child) = max(50, 25) = 50
* 50 > 40 
* swap 50 and 40
```
        50
    40       25
  45  35   10  15
20
```
* max(left child, right child) = max(45, 35) = 45
* 45 > 40 
* swap 45 and 40
```
        50
    45       25
  40  35   10  15
20
```
* max(left child, null) = 20
* 20 < 40
* stop
### Min Heap
* instead of max use mix()
* swap only if child less than parent
## Array Implementation
```
[75, 50, 25, 45, 35, 10, 15, 20, 40]
  0   1   2   3   4   5   6   7   8

        75
    50       25
  45  35   10  15
20 40
```
* save 75 into variable, then get rid of 40  return_value  = heap[0]
* swap 75 and 40 variable 
* set 45’s right child to null
```
[40, 50, 25, 45, 35, 10, 15, 20]
  0   1   2   3   4   5   6   7 

        40
    50       25
  45  35   10  15
20

left child idx = 2*idx + 1 = 0 + 1 = 1
right child idx = 2*idx + 2 = 2
max(left child, right child) = max(50, 25) = 50
```
* 50 > 40 
* swap 50 and 40
```
[50, 40, 25, 45, 35, 10, 15, 20]
  0   1   2   3   4   5   6   7 

        50
    40       25
  45  35   10  15
20
```
... and so on 
## Code
```Python
  def pop(self):
        top = self.heap[0] # save the min/max value
        # put the last element into the top position
        self.heap[0] = self.heap[self.size() - 1]
        # remove the repeat element from the last position
        self.heap.pop(self.size() - 1)
        # sift the new top value down to get the new min/max
        self.siftDown()
        return top # return the original min/max value
       
    def siftDown(self):
        nodeIdx = 0
        while nodeIdx < self.size():
            # choose min/max b/w left and right child
            childIdx = self.siftDownCompare(nodeIdx)
            # compare nodeIdx with the min/max child
            if childIdx != -1 and self.compare(nodeIdx, childIdx):
                # swap if
                # MAX: node < child -> child larger so should be on top
                # MIN: node > child -> child smaller so should be on top
                self.swap(nodeIdx, childIdx)
                nodeIdx = childIdx
            else:
                break

    def siftDownCompare(self, idx):
        isMax = self.comparator(1, 2)
        leftChildIdx = self.leftChild(idx)
        rightChildIdx = self.rightChild(idx)
        if leftChildIdx >= self.size():
            return -1
        elif leftChildIdx < self.size() and rightChildIdx >= self.size():
            return leftChildIdx
        elif rightChildIdx < self.size() and leftChildIdx >= self.size():
            return rightChildIdx
        if isMax:
            if self.heap[leftChildIdx] > self.heap[rightChildIdx]:
                return leftChildIdx
            else:
                return rightChildIdx
        else:
            if self.heap[leftChildIdx] < self.heap[rightChildIdx]:
                return leftChildIdx
            else:
                return rightChildIdx
        # MAX heap: swap node w/ max(left child, right child)
        # MIN heap: swap node w/ min(left child, right child)
    
    def leftChild(self, idx):
        return 2 * idx + 1
 
    def rightChild(self, idx):
        return 2 * idx + 2

    def swap(self, i, j):
        temp = self.heap[i];  
        self.heap[i] = self.heap[j];
        self.heap[j] = temp;
 
    def compare(self, i, j):
        return self.comparator(self.heap[i], self.heap[j]);
```
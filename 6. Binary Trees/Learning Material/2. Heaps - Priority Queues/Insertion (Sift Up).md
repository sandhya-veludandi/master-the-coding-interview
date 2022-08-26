# Insertion (Sift Up)
## Conceptual
### Max Heap 
```
     50
 40      25
20 35   10 15
```
**Insert: 45**
Insert new value into the most left position (b/c heap is complete binary tree)
```
       50
   40      25
 20 35    10 15
45
```
* Keep comparing new node (45) to parent
* **20 < 45**
* **Swap** 
```
       50
   40      25
 45 35    10 15
20
```
* **40 < 45**
* **Swap** 
```
       50
   45      25
 40 35    10 15
20
```
* **50 > 45**
* Stop


### Min Heap
Instead of swapping when new node is larger than parent node, 
swap when NEW node is SMALLER than PARENT

## Array Implementation
```
[50, 40, 25, 20, 35, 10, 15, 45]
  0   1   2   3   4   5   6  7
```
* parent of 45’s index = floor((idx - 1) / 2 ) = floor((8 - 1) / 2) = 3
→ swap 20 and 45
* parent of 45’s index = floor((idx - 1) / 2 ) = floor((3 - 1) / 2) = 1
→ swap 40 and 45
* parent of 45’s index = floor((idx - 1) / 2 ) = floor((1 - 1) / 2) = 0
→ no swap (50 is larger)

## Code
```Python
    def push(self, val):
        self.heap.append(val) # add new val to bottom of heap
        self.siftUp() # sift new val up
        return self.size()
   
    def siftUp(self):
        nodeIdx = self.size() - 1
        parent = self.parent(nodeIdx)
        # MAX heap: while the parent is smaller -> sift up: parent < node
        # MIN heap: while the parent is larger -> sift up: parent > node
        while(nodeIdx > 0 and self.compare(parent, nodeIdx)):
            # switch the parent and current node value
            self.swap(self.parent(nodeIdx), nodeIdx)
            # move node ptr to parent index
            nodeIdx = self.parent(nodeIdx)
            parent = self.parent(nodeIdx)

    def parent(self, idx):
        return math.floor((idx - 1) / 2)
 
    def compare(self, i, j):
        return self.comparator(self.heap[i], self.heap[j]);

    def swap(self, i, j):
        temp = self.heap[i];  
        self.heap[i] = self.heap[j];
        self.heap[j] = temp;
```
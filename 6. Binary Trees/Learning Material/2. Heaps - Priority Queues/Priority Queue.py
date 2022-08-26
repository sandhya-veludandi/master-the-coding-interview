import math
class PriorityQueue:
    def __init__(self, comparator):
        self.heap = []
        self.comparator = comparator

    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if not self.isEmpty():
            return self.heap[0]
        return None

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

    def parent(self, idx):
        return math.floor((idx - 1) / 2)
  
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
    
    def printHeap(self):
        if self.heap is not None:
            for i in range(len(self.heap)):
                print(i, " element: ", self.heap[i], " ")

def maxComparator(a, b):
    return a < b
def minComparator(a, b):
    return a > b

heap = PriorityQueue(maxComparator)
heap.push(50)
heap.push(40)
heap.push(25)
heap.push(20)
heap.push(35)
heap.push(10)
heap.push(15)
heap.push(45)
heap.pop()
heap.printHeap()
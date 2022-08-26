# DFS Pre-order Traversal
## Order
 root, left, right
## Example
```
         9
     4       20
  1   6    15  170

Visited Order:
[9, 4, 1, 6, 20, 15, 170]
```

## Code
```Python
def traversePreOrder(self, node, list):
  if node != None: 
    list.append(node.val)
    if node.left:
      self.traversePreOrder(node.left, list)
    if node.right:
      self.traversePreOrder(node.right, list)
    return list

def dfsPreOrder(self):
  return self.traversePreOrder(self.getRoot(), [])
```

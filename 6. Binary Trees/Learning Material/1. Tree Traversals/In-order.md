# DFS In-order Traversal
## Order
left, root, right
## Example
```
         9
     4       20
  1   6    15  170

Visited Order:
[1, 4, 6, 9, 15, 20, 170]
```

## Code
```Python
def traverseInOrder(self, node, list):
  if node != None: 
    if node.left:
      self.traverseInOrder(node.left, list)
    list.append(node.val)
    if node.right:
      self.traverseInOrder(node.right, list)
  return list

def dfsInOrder(self):
  return self.traverseInOrder(self.getRoot(), [])
```

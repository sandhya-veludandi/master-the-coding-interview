# DFS Post-order Traversal
## Order
left, right, root

## Example
```
         9
     4       20
  1   6    15  170

Visited Order:
[1, 6, 4, 15, 170, 20, 9]
```

## Code
```Python
def traversePostOrder(self, node, list):
  if node != None: 
    if node.left:
      self.traversePostOrder(node.left, list)
    if node.right:
      self.traversePostOrder(node.right, list)
    list.append(node.val)
  return list

def dfsPostOrder(self):
  return self.traversePostOrder(self.getRoot(), [])
```

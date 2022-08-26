class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inOrderTraversal(self, root, list):
        if root != None: 
            if root.left:
                self.inOrderTraversal(root.left, list)
            list.append(root.val)
            if root.right: 
                self.inOrderTraversal(root.right, list)
        return list
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        treeList = self.inOrderTraversal(root, [])
        tmpList = set(treeList)
        sortedList = sorted(treeList)
        noDuplicates = len(tmpList) == len(sortedList)
        return noDuplicates and sortedList == treeList
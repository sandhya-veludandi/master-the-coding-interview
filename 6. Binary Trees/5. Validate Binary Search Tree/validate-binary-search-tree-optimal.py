import sys
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBSTHelper(self, root, left, right): 
        if root == None: 
            return True
        # check that the node is within the current bounds otherwise return false
        if left >= root.val or root.val >= right: 
            return False
        if root.left == None and root.right == None: 
            return True
        
        leftSide = True
        rightSide = True
        if root.left != None: 
            # if going left, update the right most value to the root value
            leftSide = self.isValidBSTHelper(root.left, left, root.val)
            if not leftSide: return False
        if root.right != None: 
            rightSide = self.isValidBSTHelper(root.right, root.val, right)
            if not rightSide: return False
        return True
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, ~sys.maxsize, sys.maxsize)
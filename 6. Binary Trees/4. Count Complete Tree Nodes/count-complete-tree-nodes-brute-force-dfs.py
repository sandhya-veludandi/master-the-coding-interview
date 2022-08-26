class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def countNodesHelper(self, root, count): 
        if root == None: 
            return 0
        else: 
            count += 1
            leftSide = 0
            rightSide = 0
            if root.left != None: 
                leftSide = self.countNodesHelper(root.left, 0)
            if root.right != None: 
                rightSide = self.countNodesHelper(root.right, 0)
            count += (leftSide + rightSide)
            return count
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countNodesHelper(root, 0)
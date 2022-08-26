class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxHeight(self, root): 
        if root == None: 
            return 0
        leftHeight = 1 + self.maxHeight(root.left)
        rightHeight = 1 + self.maxHeight(root.right)
        return max(leftHeight, rightHeight)
    
    def countNodesHelper(self, root, h, currHeight, numNodes): 
        if root == None: 
            return numNodes
    
        if root.left == None: 
            numNodes += 1
            return numNodes
        else: 
            left = self.maxHeight(root.left)
            right = self.maxHeight(root.right)
            if right >= left: 
                numNodes += pow(2, h-1-currHeight)
                currHeight+=1
                return self.countNodesHelper(root.right, h, currHeight, numNodes)
            else: 
                currHeight+=1
                return self.countNodesHelper(root.left, h, currHeight, numNodes)
            
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        h = self.maxHeight(root)
        numNodes = pow(2, h-1)-1
        currHeight = 1
        numNodes = self.countNodesHelper(root, h, currHeight, numNodes)
        return numNodes
        
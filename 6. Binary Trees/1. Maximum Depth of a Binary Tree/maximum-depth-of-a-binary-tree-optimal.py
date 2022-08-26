class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepthHelper(self, root, count): 
        if root == None: 
            return count
        count += 1
        return max(self.maxDepthHelper(root.left, count),        self.maxDepthHelper(root.right, count))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDepthHelper(root, 0)
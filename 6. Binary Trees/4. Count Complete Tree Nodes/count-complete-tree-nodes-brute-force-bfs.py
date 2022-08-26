class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        queue = []
        curr = root
        queue.append(curr)
        orderOfNodesList = []
        while queue != []: 
            curr = queue[0]
            orderOfNodesList.append(curr)
            queue = queue[1:]
            if curr.left: 
                queue.append(curr.left)
            if curr.right != None: 
                queue.append(curr.right)
        return len(orderOfNodesList)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        curr = root
        queue = []
        queue.append(curr)
        tempList = []
        rightNodes = []
        length = 1
        count = 0
        while queue != []: 
            curr = queue[0]
            tempList.append(curr.val)
            count += 1
            queue = queue[1:]
            
            if curr.left: 
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
            if length == count: 
                rightNodes.append(tempList[-1])
                tempList = []
                count = 0
                length = len(queue)
            
        return rightNodes
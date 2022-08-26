class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):   
    def helper(self, node, list, height):
        if node == None: 
            return list
        height += 1
        if height - 1 == len(list): 
            list.append(node.val)

        if node.right:
            self.helper(node.right, list, height)

        if node.left:
            self.helper(node.left, list, height)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.helper(root, [], 0)
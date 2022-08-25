class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        while curr != None: 
            print(curr.val)
            if curr.child != None: 
                temp = curr.next
                curr.next = curr.child
                curr.child = None
                curr.next.prev = curr
                tail = curr
                while tail != None: 
                    if tail.next == None: 
                        break
                    tail = tail.next
                tail.next = temp
                if temp != None:
                    temp.prev = tail
            curr = curr.next
            
        return head
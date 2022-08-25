class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        prev = head
        while curr != None and curr.next != None:
            curr = curr.next.next
            prev = prev.next
            if curr != None and curr == prev:
              return True
        return False
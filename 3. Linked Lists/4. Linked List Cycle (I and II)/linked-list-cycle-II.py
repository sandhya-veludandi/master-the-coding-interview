class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = head
        while curr != None and curr.next != None:
            curr = curr.next.next
            prev = prev.next
            if curr != None and curr == prev:
                start = head
                while start != curr:
                    start = start.next
                    curr = curr.next
                return start
        return None
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        #create new list
        newHead = None
        #create a new node and add it to the to the front of the list
        while head is not None:
            newNode = ListNode(val=head.val, next=newHead)
            newHead = newNode
            head = head.next
        return newHead
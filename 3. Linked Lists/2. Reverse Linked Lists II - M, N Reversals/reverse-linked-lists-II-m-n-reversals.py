class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        if head == None or head.next == None: 
            return head
        count = 1
        big_prev = None
        tail = None
        prev = None
        curr = head
        while(curr):
            if left <= count and count <= right: 
                if(count == left): 
                    tail = curr
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                if count == right: 
                    tail.next = temp
                    if big_prev != None: 
                        big_prev.next = prev
                        return head
                    else:
                        return prev
                    
            else: 
                big_prev = curr
                curr = curr.next
            count += 1
from collections import deque
class MyQueue(object):

    def __init__(self):
        self.elements = deque()
        self.save = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.elements.append(x)
        

    def pop(self):
        """
        :rtype: int
        """ 
        while len(self.elements) > 0: 
            self.save.append(self.elements.pop())
        result = self.save.pop()
        while len(self.save) > 0: 
            self.elements.append(self.save.pop())
        return result
        

    def peek(self):
        """
        :rtype: int
        """
        while len(self.elements) > 0: 
            self.save.append(self.elements.pop())
        result = self.save.pop()
        self.save.append(result)
        while len(self.save) > 0: 
            self.elements.append(self.save.pop())
        return result
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.elements) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1: return False
        
        stack = []
        valid = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c not in valid: 
                stack.append(c)
            elif stack != [] and valid[c] == stack[-1]: 
                stack.pop()
            else: 
                return False
        return stack == []
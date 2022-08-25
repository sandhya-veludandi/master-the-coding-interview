import re
def minRemoveToMakeValid(self, s):
    """
    :type s: str
    :rtype: str
    """
    stackIndices = []
    s = list(s)
    print(s)
    i = 0
    while i < len(s):
        #if we have close parens match
        if stackIndices != [] and s[i] == ')' and s[stackIndices[-1]] == '(': 
            stackIndices.pop()
        elif stackIndices == [] and s[i] == ')': 
            del s[i]
            i -= 1
        elif s[i] == '(' or s[i] == ')': 
            stackIndices.append(i)
        i += 1
    
    while stackIndices != []: 
        idx = stackIndices.pop()
        del s[idx]
    return "".join(s)
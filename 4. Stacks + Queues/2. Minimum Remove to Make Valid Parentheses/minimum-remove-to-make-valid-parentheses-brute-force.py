import re
def minRemoveToMakeValid(self, s):
    """
    :type s: str
    :rtype: str
    """
    stackParens = []
    stackIndices = []
    for i in range(len(s)):
        char = s[i]
        #if we have close parens match
        if stackParens != [] and char == ')' and stackParens[-1] == '(': 
            stackParens.pop()
            stackIndices.pop()
        elif char == '(' or char == ')': 
            stackParens.append(char)
            stackIndices.append(i)
    #remove the parens using stackIndices
    arr1=[]
    for i in range(len(s)):
        arr1.append(i)
    new = filter(lambda i: i not in stackIndices, arr1)
    new_str = ""
    for i in new: 
        new_str += s[i]
    return new_str
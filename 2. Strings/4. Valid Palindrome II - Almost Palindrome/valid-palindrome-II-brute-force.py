import re
def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    if s == s[::-1]: 
        return True
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            #add two possible palindromes
            #one without i char
            s1 = s[:i]+s[i+1:]
            #one without len(s)-1-i char
            s2 = s[:len(s)-1-i]+s[len(s)-i:]
            
            return s1 == s1[::-1] or s2 == s2[::-1]
import re
def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    if s == s[::-1]: 
        return True
    i = 0
    while i < len(s)/2+1:
        if s[i] != s[len(s)-1-i]:
            #two possible palindromes
            #one with i char and without len(s)-1-i
            s1 = s[i:len(s)-1-i]
            #one with len(s)-1-i char and without i
            s2 = s[i+1:len(s)-i]
            return s1 == s1[::-1] or s2 == s2[::-1]
        i += 1
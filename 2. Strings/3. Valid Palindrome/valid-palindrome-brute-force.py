import re
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
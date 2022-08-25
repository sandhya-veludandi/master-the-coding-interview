import re
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return s == s[::-1]
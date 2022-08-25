def longestSubstringWithoutRepeats(s):
    """
    :type s: str
    :rtype: int
    """
    chars = {}
    left = 0
    right = 0
    maxLength = 0
    while right < len(s):
        curr_char = s[right]
        prevSeenChar = -1
        if curr_char in chars:
            prevSeenChar = chars[curr_char]
        if prevSeenChar >= left:
            prevSeenChar += 1
            left = prevSeenChar
        chars[curr_char] = right
        maxLength = max(right-left+1, maxLength)
        right += 1
    return maxLength
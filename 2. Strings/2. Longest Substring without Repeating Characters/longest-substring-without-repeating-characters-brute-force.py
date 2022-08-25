def longestSubstringWithoutRepeats(s):
    """
    :type s: str
    :rtype: int
    """
    curr_index = 0
    maxLength = 0
    chars = {}
    while curr_index < len(s):
        if s[curr_index] not in chars:
            chars[s[curr_index]] = curr_index
        else:
            curr_index = chars[s[curr_index]]+1
            chars = {}
            chars[s[curr_index]] = curr_index
        maxLength = max(maxLength, len(chars))
        curr_index += 1
    return maxLength
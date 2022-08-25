def backspaceCompare(self, s, t):
    """ 
    :type s: str
    :type t: str
    :rtype: bool
    """
    p1 = len(s) - 1
    p2 = len(t) - 1        
    stepS = 0
    stepT = 0
    
    while p1 >= 0 or p2 >= 0:
        #as long as p1 is not negative
        while p1 >= 0:
            #if find # then move on to the next char, and increase stepS
            if s[p1] == "#":
                p1 -= 1
                stepS +=1
            #if there are stepS (chars to skip) then move on to next char and decrease the number of stepS to skip
            elif stepS > 0:
                p1 -= 1
                stepS -= 1
            #if there are no chars to skip, (no #'s or no chars before #'s), then break
            else:
                break  
                
        while p2 >= 0:
            if t[p2] == "#":
                p2 -= 1
                stepT +=1
            elif stepT > 0:
                p2 -= 1
                stepT -= 1
            else:
                break
                
        #if both indices are negative, then return true
        #if both indices ended but one is negative and the other is not, then return false
        if p1 < 0: return p2 < 0            
        if p2 < 0: return p1 < 0     
        #if the chars are not #'s or chars before #'s and do not equal each other, return false           
        if s[p1] != t[p2]: return False
        #if the characters are equal, then check the rest of the string
        p1 -= 1
        p2 -= 1             

    return True
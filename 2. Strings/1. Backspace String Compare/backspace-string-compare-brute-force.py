def resultString(self, s): 
        result = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                if i > 0 and len(result) > 0:
                    result.pop()
            else: 
                result.append(s[i])
            i += 1
        return result
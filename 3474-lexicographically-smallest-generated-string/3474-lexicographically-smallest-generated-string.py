class Solution(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        n = len(str1)
        m = len(str2)
        l = m + n - 1

        s = ['a'] * l
        fixed = [False] * l

        for i, ch in enumerate(str1):
            if ch == "T":
                
                for j, c in enumerate(str2, i):
                    if fixed[j] and s[j] != c:
                        return ""
                    
                    s[j] = c
                    fixed[j] = True
        
        for i, ch in enumerate(str1):
            if ch == "F":
                if any(str2[j - i] != s[j] for j in range(i, i + m)):
                    continue
                
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        s[j] = "b"
                        break

                else:
                    return ""
        
        return "".join(s)
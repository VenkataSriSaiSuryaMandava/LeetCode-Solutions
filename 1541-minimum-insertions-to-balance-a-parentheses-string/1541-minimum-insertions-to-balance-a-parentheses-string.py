class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        count = 0

        i = 0
        n = len(s)

        while i < len(s):
            if s[i] == '(':
                count += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    res += 1

                if count == 0:
                    res += 1
                else:
                    count -= 1
            
            i += 1
        
        if count > 0:
            res += count << 1

        return res
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        group = []

        while i < len(s):
            count = 1

            while i  + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
                
            group.append(count)
            i += 1
        
        res = 0
        for i in range(1, len(group)):
            res += min(group[i], group[i - 1])
        
        return res
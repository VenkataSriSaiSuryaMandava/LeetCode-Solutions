class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        res = 0
        maxZero = 0
        pre = float("-inf")

        l = 0
        r = 0

        while r < len(s):
            while r < len(s) and s[l] == s[r]:
                r += 1
            
            cur = r - l

            if s[l] == '1':
                res += cur
            else:
                maxZero = max(maxZero, pre + cur)
                pre = cur
            
            l = r
        
        return res + maxZero
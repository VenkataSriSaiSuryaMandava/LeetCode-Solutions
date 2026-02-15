class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            resLen, res = self.helper(s, i , i, resLen, res)
            resLen, res = self.helper(s, i, i + 1, resLen, res)
        
        return res

    def helper(self, s, l, r, resLen, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
            
            return (resLen, res)
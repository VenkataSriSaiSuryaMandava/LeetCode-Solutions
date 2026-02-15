class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def helper(l, r, resLen, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
            
            return (resLen, res)
        
        for i in range(len(s)):
            resLen, res = helper(i , i, resLen, res)
            resLen, res = helper(i, i + 1, resLen, res)
        
        return res
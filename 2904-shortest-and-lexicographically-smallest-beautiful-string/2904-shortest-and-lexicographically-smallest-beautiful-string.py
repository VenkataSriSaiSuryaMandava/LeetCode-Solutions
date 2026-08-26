class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        count = 0
        l = 0

        for r in range(len(s)):
            if s[r] == '1':
                count += 1
            
            while count == k:
                sub = s[l : r + 1]

                if not res or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                    res = sub

                if s[l] == '1':
                    count -= 1
                l += 1
        
        return res
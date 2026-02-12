class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        sset = set()
        
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l += 1
            sset.add(s[r])
            res = max(res, r - l + 1)
        return res
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == len(s)
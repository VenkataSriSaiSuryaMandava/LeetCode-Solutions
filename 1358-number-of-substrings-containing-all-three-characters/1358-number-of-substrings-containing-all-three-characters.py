class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastIndexes = {'a' : -1, 'b' : -1, 'c' : -1}
        res = 0

        for i, ch in enumerate(s):
            lastIndexes[ch] = i
            res += min(lastIndexes.values()) + 1
        
        return res
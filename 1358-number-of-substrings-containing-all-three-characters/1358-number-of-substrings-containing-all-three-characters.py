class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastIndex = {'a' : -1, 'b' : -1, 'c' : -1}
        res = 0

        for i, ch in enumerate(s):
            lastIndex[ch] = i
            res += min(lastIndex['a'], lastIndex['b'], lastIndex['c']) + 1
        
        return res
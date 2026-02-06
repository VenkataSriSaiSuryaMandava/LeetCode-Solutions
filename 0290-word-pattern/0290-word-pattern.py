class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        mapps = {}
        mapsp = {}

        for c1, c2 in zip(pattern, s):
            if c1 in mapps and mapps[c1] != c2 or c2 in mapsp and mapsp[c2] != c1:
                return False
            mapps[c1] = c2
            mapsp[c2] = c1
        return True
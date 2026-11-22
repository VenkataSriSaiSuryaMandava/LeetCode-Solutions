class Solution:
    def checkString(self, s: str) -> bool:
        aIdx = -1
        bIdx = float("inf")

        for idx, ch in enumerate(s):
            if ch == 'a':
                aIdx = idx
            if ch == 'b' and bIdx == float("inf"):
                bIdx = idx
        
        return aIdx < bIdx
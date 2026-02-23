class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        visit = set()
        for i in range(len(s) - k + 1):
            visit.add(s[i : i + k])
        
        return len(visit) == 2 ** k
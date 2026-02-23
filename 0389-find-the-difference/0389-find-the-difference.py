class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        Count = defaultdict(int)

        for ch in t:
            Count[ch] += 1
        
        for ch in s:
            Count[ch] -= 1
        
        for key, val in Count.items():
            if val == 1:
                return key
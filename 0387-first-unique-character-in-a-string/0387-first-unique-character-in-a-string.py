class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for ch in s:
            count[ch] += 1
        
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        
        return -1
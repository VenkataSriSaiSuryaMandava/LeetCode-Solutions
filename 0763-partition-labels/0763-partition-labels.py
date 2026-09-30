class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastIndex = {}

        for i, ch in enumerate(s):
            lastIndex[ch] = i
        
        res = []
        end = 0
        size = 0

        for i, ch in enumerate(s):
            size += 1
            end = max(end, lastIndex[ch])

            if i == end:
                res.append(size)
                size = 0
        
        return res
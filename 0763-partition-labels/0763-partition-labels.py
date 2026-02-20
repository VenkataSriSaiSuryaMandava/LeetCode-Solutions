class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        LastIndex= {}
        for i, c in enumerate(s):
            LastIndex[c] = i
        
        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, LastIndex[c])

            if end == i:
                res.append(size)
                size = 0
        
        return res
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        level = 0

        for ch in seq:
            if ch == '(':
                if level % 2:
                    res.append(0)
                else:
                    res.append(1)
                
                level += 1
            else:
                level -= 1

                if level % 2:
                    res.append(0)
                else:
                    res.append(1)
        
        return res
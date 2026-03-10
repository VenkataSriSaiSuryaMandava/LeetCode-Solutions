class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for s in spells:
            idx = len(potions)
            l = 0
            r = len(potions) - 1

            while l <= r:
                m = (l + r) // 2

                if potions[m] * s >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            
            res.append(len(potions) - idx)
        
        return res
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []

        for c in candies:
            res.append(c + extraCandies >= maxCandies)
        
        return res
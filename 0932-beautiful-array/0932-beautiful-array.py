class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        
        leftSide = self.beautifulArray((n + 1) // 2)
        rightSide = self.beautifulArray(n // 2)

        odd_numbers = [2 * x - 1 for x in leftSide]
        even_numbers = [2 * x for x in rightSide]

        return odd_numbers + even_numbers
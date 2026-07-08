class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 and high % 2:
            count = high - low + 1
        elif low % 2 or high % 2:
            count = high - low
        else:
            count = high - low - 1
        
        return (count + 1) // 2
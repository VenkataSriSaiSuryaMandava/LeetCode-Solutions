class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def countBits(n):
            count = 0
            while n:
                n = n & (n - 1)
                count += 1
            return count
        
        return sorted(arr, key = lambda x : (countBits(x), x))
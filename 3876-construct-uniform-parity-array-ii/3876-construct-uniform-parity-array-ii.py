class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float("inf")

        for num in nums1:
            if num % 2:
                minOdd = min(minOdd, num)
        
        if minOdd == float("inf"):
            return True
        
        for num in nums1:
            if num % 2 == 0 and num < minOdd:
                return False
        
        return True
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        even = 0
        odd = 0

        for num in nums1:
            if num % 2:
                odd += 1
            else:
                even += 1
        
        return n == 1 or odd == 0 or even == 0 or (even >= 1 and odd >= 1)
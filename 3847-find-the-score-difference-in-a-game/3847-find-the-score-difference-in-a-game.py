class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        first_active = True
        s1 = 0
        s2 = 0

        for i, x in enumerate(nums):
            if x % 2:
                first_active = not first_active

            if (i + 1) % 6 == 0:
                first_active = not first_active
                
            if first_active:
                s1 += x
            else:
                s2 += x

        return s1 - s2
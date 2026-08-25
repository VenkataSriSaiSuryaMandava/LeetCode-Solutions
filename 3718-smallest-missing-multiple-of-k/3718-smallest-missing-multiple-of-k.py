class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numsSet = set(nums)
        i = 1

        while i * k in numsSet:
            i = i + 1
        
        return i * k
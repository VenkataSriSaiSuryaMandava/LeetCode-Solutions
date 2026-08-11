class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        numsSet = set(nums)
        prefix = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                prefix += nums[i]
            else:
                break
        
        while prefix in numsSet:
            prefix += 1
                
        return prefix
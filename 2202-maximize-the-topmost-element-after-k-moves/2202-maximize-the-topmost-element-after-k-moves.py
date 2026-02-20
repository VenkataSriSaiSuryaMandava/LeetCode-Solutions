class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if  k == 0:
            return nums[0]

        if len(nums) == 1:
            if k % 2:
                return -1
            else:
                return nums[0]
        
        res = max(nums[ : k - 1], default = -1)

        if k < len(nums):
            res = max(res, nums[k])
        
        return res

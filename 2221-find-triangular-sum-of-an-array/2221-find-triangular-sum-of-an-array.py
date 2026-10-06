class Solution:
    def triangularSum(self, nums: list[int]) -> int:        
        while len(nums) > 1:
            newNums = [0] * (len(nums) - 1)

            for i in range(len(newNums)):
                newNums[i] = (nums[i] + nums[i + 1]) % 10
            
            nums = newNums

        return nums[0]
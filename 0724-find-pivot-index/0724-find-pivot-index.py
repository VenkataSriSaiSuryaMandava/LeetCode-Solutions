class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums)
        curSum = 0
        
        for i in range(len(nums)):
            leftSum[i] = curSum
            curSum += nums[i]
        
        rightSum = [0] * len(nums)
        curSum = 0

        for i in range(len(nums) - 1, -1, -1):
            rightSum[i] = curSum
            curSum += nums[i]
        
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        
        return -1
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = sum(nums)

        res = []

        for num in nums:
            rightSum -= num
            res.append(abs(leftSum - rightSum))
            leftSum += num
                    
        return res
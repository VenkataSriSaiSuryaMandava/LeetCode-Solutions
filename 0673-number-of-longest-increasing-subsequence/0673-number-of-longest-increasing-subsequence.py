class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lenLIS = 0
        res = 0

        for i in range(len(nums) - 1, -1, -1):
            maxLen = 1
            maxCount = 1

            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    length, count = dp[j]

                    if length + 1 > maxLen:
                        maxLen, maxCount = length + 1, count
                    elif length + 1 == maxLen:
                        maxCount += count
            
            dp[i] = [maxLen, maxCount]
            
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCount
            elif maxLen == lenLIS:
                res += maxCount
        
        return res
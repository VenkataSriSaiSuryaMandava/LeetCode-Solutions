class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        maxProduct = lcm(*nums) * gcd(*nums)

        for i in range(n):
            curProduct = 1
            curLcm = 1
            curGcd = 0

            for j in range(i, n):
                curProduct *= nums[j]
                curLcm = lcm(curLcm, nums[j])
                curGcd = gcd(curGcd, nums[j])

                if curProduct == curLcm * curGcd:
                    res = max(res, j - i + 1)
                
                if curProduct > maxProduct:
                    break
        
        return res
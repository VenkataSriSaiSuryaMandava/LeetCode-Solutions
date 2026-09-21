class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k
        
        for num in nums:
            v = num % k
            next_dp = [0] * k
            next_dp[v] += 1
            
            for rem in range(k):
                if dp[rem]:
                    next_dp[(rem * v) % k] += dp[rem]
            
            for rem in range(k):
                result[rem] += next_dp[rem]
                
            dp = next_dp
            
        return result
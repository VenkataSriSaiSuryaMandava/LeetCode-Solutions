class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set([0])
        target = sum(nums) // 2

        for n in nums:
            newDP = set()

            for t in dp:
                if n + t == target:
                    return True
                
                newDP.add(t)
                newDP.add(n + t)
            
            dp = newDP
        
        return False
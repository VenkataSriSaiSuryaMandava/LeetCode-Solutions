class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        
        target = sum(nums) // k
        used = [False] * len(nums)

        nums.sort(reverse = True)

        def backtrack(i, k, curSum):
            if k == 0:
                return True
            
            if curSum == target:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if (used[j] or nums[j] + curSum > target or 
                    (i < j and nums[j] == nums[j - 1] and not used[j - 1])):
                    continue
                
                used[j] = True
                
                if backtrack(j + 1, k, curSum + nums[j]):
                    return True
                
                used[j] = False
            
            return False
        
        return backtrack(0, k, 0)
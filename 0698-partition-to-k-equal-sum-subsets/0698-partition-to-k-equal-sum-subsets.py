class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        nums.sort(reverse = True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, curSum):
            if k == 0:
                return True
            
            if curSum == target:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or curSum + nums[j] > target or (j > i and nums[j] == nums[j - 1] and not used[j - 1]):
                    continue

                used[j] = True

                if backtrack(j + 1, k, curSum + nums[j]):
                    return True
                
                used[j] = False
            
            return False
        
        return backtrack(0, k, 0)
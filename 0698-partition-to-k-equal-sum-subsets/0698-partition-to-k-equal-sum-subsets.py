class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k:
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
                if (used[j] or curSum + nums[j] > target or (i < j and 
                    nums[j - 1] == nums[j] and not used[j - 1])): 
                    continue
                
                used[j] = True

                if backtrack(j + 1, k, curSum + nums[j]):
                    return True
                
                used[j] = False
            
            return False
        
        return backtrack(0, k, 0)
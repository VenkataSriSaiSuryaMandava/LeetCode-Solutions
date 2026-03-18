class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsetSum = sum(nums) // k
        subsets = [0] * k

        if sum(nums) / k != subsetSum:
            return False
        
        nums.sort(reverse = True)

        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] > subsetSum:
                    continue
                
                subsets[j] += nums[i]

                if backtrack(i + 1):
                    return True
                
                subsets[j] -= nums[i]

                if subsets[j] == 0:
                    break
            
            return False
        
        return backtrack(0)
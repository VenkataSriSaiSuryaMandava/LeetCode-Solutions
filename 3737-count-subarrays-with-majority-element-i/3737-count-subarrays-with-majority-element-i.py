class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0

        for i in range(len(nums)):
            count = 0

            for j in range(i, len(nums)):
                if nums[j] == target:
                    count += 1
                
                length = j - i + 1
                
                if 2 * count > length:
                    res += 1
        
        return res
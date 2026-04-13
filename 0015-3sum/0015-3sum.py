class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            if num == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
        
        return res
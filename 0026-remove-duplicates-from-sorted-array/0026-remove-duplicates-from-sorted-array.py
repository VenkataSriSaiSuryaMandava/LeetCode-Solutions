class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums or len(nums) == 1:    return len(nums)
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[i],nums[start]=nums[start],nums[i]
        return start+1
            

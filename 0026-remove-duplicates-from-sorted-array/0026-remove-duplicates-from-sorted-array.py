class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums or len(nums) == 1:    return len(nums)
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)
        
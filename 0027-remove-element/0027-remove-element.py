class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        end = i = len(nums)-1
        while i >= 0:
            if nums[i] == val:
                nums[i],nums[end] = nums[end], nums[i]
                end -= 1
            i -= 1
        return end+1
        
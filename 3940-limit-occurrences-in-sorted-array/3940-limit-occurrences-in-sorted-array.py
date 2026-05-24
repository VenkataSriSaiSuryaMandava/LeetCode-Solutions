class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        l = 0

        for num in nums:
            if l < k or nums[l - k] != num:
                nums[l] = num
                l += 1

        return nums[ : l]
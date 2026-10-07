class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev_arr(i, j):
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if not nums or len(nums) == 1:    return
        if len(nums) == 2:
            nums[0],nums[1] = nums[1],nums[0]
            return
        l = len(nums)
        i = l-2
        while i>=0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                break
        if i < 0:
            rev_arr(0, l-1)
            return
        left, nLeft = i, nums[i]
        i = l-1
        while i>=0:
            if nums[i] > nLeft:
                nums[i], nums[left] = nums[left], nums[i]
                print(nums)
                rev_arr(left+1, l-1)
                return
            i -= 1


        
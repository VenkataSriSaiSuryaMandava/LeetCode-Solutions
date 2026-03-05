class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                res = [m, m]
                i = m
                while i - 1 >= 0 and nums[i - 1] == nums[i]:
                    i -= 1
                res[0] = i

                i = m
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                res[1] = i
                break
        return res
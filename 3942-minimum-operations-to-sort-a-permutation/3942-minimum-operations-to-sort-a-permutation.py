class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        res = float("inf")

        increasing = True

        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                increasing = False
                break

        if increasing:
            start = nums[0]

            direct = (n - start) % n
            with_reverse = start + 2

            res = min(res, direct, with_reverse)

        decreasing = True

        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] - 1) % n:
                decreasing = False
                break

        if decreasing:
            start = nums[0]

            reverse_first = 1 + ((n - start - 1) % n)
            rotate_first = start + 2

            res = min(res, reverse_first, rotate_first)

        return res if res != float("inf") else -1
            
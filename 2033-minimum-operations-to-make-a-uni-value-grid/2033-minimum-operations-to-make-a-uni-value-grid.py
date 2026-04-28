class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        for row in grid:
            for n in row:
                if n % x != grid[0][0] % x:
                    return -1
        
        nums = [n for row in grid for n in row]
        nums.sort()

        res = float("inf")
        total = sum(nums)
        prefix = 0

        for i in range(len(nums)):
            left_cost = nums[i] * i - prefix
            right_cost = total - prefix - (nums[i] * (len(nums) - i))

            operations = (left_cost + right_cost) // x
            res = min(res, operations)

            prefix += nums[i]
        
        return res
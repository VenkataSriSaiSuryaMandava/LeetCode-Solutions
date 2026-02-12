class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        nums = [i for i in range(1, n + 1)]

        def dfs(i):
            if len(subset) == k:
                res.append(subset.copy())
                return

            if i == n:
                return
                
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        dfs(0)

        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return 
            
            for n in count:
                if count[n] > 0:
                    perms.append(n)
                    count[n] -= 1
                    dfs()

                    perms.pop()
                    count[n] += 1
        dfs()
        return res
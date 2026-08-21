class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        res = []
        perms = []

        def backtrack():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            
            for num in perms:
                if count[num]:
                    count[num] -= 1
                    perms.append(num)
                    backtrack()

                    count[num] += 1
                    perms.pop()
        
        backtrack()
        return res
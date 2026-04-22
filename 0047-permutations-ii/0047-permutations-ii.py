class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        res = []
        perms = []

        def backtrack():
            if len(perms) == len(nums):
                res.append(perms[ : : ])
                return 
            
            for n in count:
                if count[n]:
                    count[n] -= 1
                    perms.append(n)
                    backtrack()
                    
                    count[n] += 1
                    perms.pop()
        
        backtrack()

        return res
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]

        for n in nums:
            newPerms = []

            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p[ : :]
                    pCopy.insert(i, n)
                    newPerms.append(pCopy)
            
            perms = newPerms
        
        return perms
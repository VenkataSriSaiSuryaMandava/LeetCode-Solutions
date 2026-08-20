class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            newPerms = []

            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    newPerms.append(pCopy)
            
            perms = newPerms
        
        return perms
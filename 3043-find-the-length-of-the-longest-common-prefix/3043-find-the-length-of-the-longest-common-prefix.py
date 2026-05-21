class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arrSet = set()
        res = 0

        for n in arr1:
            n = str(n)

            for i in range(1, len(n) + 1):
                arrSet.add(n[ : i])
        
        for n in arr2:
            n = str(n)

            for i in range(1, len(n) + 1):
                if n[ : i] in arrSet:
                    res = max(res, len(n[ : i]))
        
        return res
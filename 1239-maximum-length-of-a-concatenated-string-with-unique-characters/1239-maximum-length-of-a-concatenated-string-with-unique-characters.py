class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        charSet = set()

        def overlap(s):
            prev = set()

            for c in s:
                if c in prev or c in charSet:
                    return True
                
                prev.add(c)

            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            
            res = 0

            if not overlap(arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                
                res = backtrack(i + 1)

                for c in arr[i]:
                    charSet.remove(c)
            
            return max(res, backtrack(i + 1))

        return backtrack(0)
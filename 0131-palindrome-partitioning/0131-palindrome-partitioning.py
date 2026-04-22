class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True
        
        res = []
        subset = []

        def backtrack(i):
            if i == len(s):
                res.append(subset[ : :])
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    subset.append(s[i : j + 1])
                    backtrack(j + 1)
                    subset.pop()
        
        backtrack(0)

        return res
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def plaindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return plaindrome(l + 1, r) or plaindrome(l, r - 1)
            
            l += 1
            r -= 1
        
        return True
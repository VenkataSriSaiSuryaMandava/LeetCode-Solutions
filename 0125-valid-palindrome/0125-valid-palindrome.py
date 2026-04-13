class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphaNum(ch):
            return (ord("A") <= ord(ch) <= ord("Z") or
                    ord("a") <= ord(ch) <= ord("z") or
                    ord("0") <= ord(ch) <= ord("9"))
        
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
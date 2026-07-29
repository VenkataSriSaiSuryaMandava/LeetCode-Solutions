class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(ch):
            return (ord('0') <= ord(ch) <= ord('9') or
                    ord('a') <= ord(ch) <= ord('z') or
                    ord('A') <= ord(ch) <= ord('Z'))
        
        def toLower(ch):
            if ord('A') <= ord(ch) <= ord('Z'):
                return chr(ord('a') + (ord(ch) - ord('A')))
            else:
                return ch

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            
            if toLower(s[l]) != toLower(s[r]):
                return False
            
            l += 1
            r -= 1
        
        return True

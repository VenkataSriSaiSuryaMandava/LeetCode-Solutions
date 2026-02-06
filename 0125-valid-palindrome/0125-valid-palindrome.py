class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalphanum(ch):
            return (ord('A') <= ord(ch) <= ord('Z') or
                    ord('a') <= ord(ch) <= ord('z') or
                    ord('0') <= ord(ch) <= ord('9'))

        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not isalphanum(s[i]): 
                i += 1
            while i < j and not isalphanum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
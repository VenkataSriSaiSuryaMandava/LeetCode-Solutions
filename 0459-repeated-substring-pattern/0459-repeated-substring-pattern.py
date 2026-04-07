class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cur = ""
        length = len(s)

        for c in s:
            cur += c
            if len(cur) == length:
                break
                
            if length % len(cur) == 0:
                if s == cur * (length // len(cur)):
                    return True
        
        return False
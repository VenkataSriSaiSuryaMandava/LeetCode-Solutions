class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 1
        setS = set()

        i = 0
        while i < len(s):
            if s[i] in setS:
                setS = set()
                res += 1
            
            setS.add(s[i])
            i += 1
        
        return res
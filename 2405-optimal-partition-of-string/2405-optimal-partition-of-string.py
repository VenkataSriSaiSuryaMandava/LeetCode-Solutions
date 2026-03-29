class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        res = 1

        for c in s:
            if c in seen:
                res += 1
                seen = set()
            
            seen.add(c)

        return res
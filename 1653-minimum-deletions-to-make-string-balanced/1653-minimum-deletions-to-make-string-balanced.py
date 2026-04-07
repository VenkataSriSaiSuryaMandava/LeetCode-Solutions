class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_count_right = 0
        b_count_left = 0
        res = len(s)

        for c in s:
            if c == "a":
                a_count_right += 1
        
        for i, c in enumerate(s):
            if c == "a":
                a_count_right -= 1
            
            res = min(res, a_count_right + b_count_left)

            if c == "b":
                b_count_left += 1
        
        return res
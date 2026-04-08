class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)
        freq  = set()
        res = 0

        for c in s:
            count[c] += 1

        count = dict(sorted(count.items(), key = lambda item : item[1], reverse = True)) 

        for key, val in count.items():
            while val in freq:
                val -= 1
                res += 1
            
            freq.add(val)

        return res
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        res = 0
        count = defaultdict(int)
        freq = 0

        for r in range(len(s)):
            count[s[r]] += 1
            freq = max(freq, count[s[r]])

            if (r - l + 1) - freq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
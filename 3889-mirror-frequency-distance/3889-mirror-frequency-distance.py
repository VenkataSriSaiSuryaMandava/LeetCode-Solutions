class Solution(object):
    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)
        res = 0
        seen = set()

        for c in s:
            count[c] += 1
            
        for c in s:
            if c in seen:
                continue
                
            if c in "0123456789":
                m = chr(ord('0') + ord('9') - ord(c))
            else:
                m = chr(ord('a') + ord('z') - ord(c))

            res += abs(count[c] - count[m])

            seen.add(c)
            seen.add(m)

        return res
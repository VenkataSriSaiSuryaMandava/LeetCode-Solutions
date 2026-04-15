class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        res = n

        for i, word in enumerate(words):
            if word == target:
                dist = abs(i - startIndex)
                res = min(res, dist, n - dist)
        
        return res if res != n else -1
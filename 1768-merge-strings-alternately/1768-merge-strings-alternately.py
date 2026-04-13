class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        l = 0
        r = 0

        while l < len(word1) and r < len(word2):
            res.append(word1[l])
            res.append(word2[r])

            l += 1
            r += 1
        
        if l < len(word1):
            res.append(word1[l : ])
        
        if r < len(word2):
            res.append(word2[r : ])
        
        return "".join(res)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        countS = defaultdict(int)
        countT = defaultdict(int)

        for ch in s:
            countS[ch] += 1
        
        for ch in t:
            countT[ch] += 1
        
        return countT == countS
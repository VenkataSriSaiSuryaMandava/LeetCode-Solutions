class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        r = 0

        while r < len(s):
            while r < len(s) and s[r] == " ":
                r += 1
            
            l = r
            while r < len(s) and s[r] != " ":
                r += 1
            
            if l < r:
                words.append(s[l : r])
        
        words.reverse()
        return " ".join(words)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        for i in range(len(strs[0])):
            for str in strs:
                if i >= len(str) or str[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
        
        return res
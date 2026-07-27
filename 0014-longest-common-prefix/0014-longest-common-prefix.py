class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i] or len(word) <= i:
                    return res
            
            res += strs[0][i]
        
        return res
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if s1[0] == s2[2]:
            s1 = s1[2] + s1[1] + s1[0] + s1[3]

        if s1[1] == s2[3]:
            s1 = s1[0] + s1[3] + s1[2] + s1[1]
        
        return s1 == s2
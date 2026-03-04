class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(p)):
            count1[ord(p[i]) - ord('a')] += 1
            count2[ord(s[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        l = 0
        res = []
        for r in range(len(p), len(s)):
            if matches == 26:
                res.append(l)
            
            index = ord(s[r]) - ord('a')
            count2[index] += 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] + 1 == count2[index]:
                matches -= 1

            index = ord(s[l]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1
            l += 1
        if matches == 26:
            res.append(l)
        return res

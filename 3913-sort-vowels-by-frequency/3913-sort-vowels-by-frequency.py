class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        countVowels = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
        indexVowels = {}

        for i, ch in enumerate(s):
            if ch in countVowels:
                countVowels[ch] += 1

                if ch not in indexVowels:
                    indexVowels[ch] = i
        
        sortedVowels = sorted(
            [v for v in countVowels if countVowels[v] > 0],
            key = lambda x : (-countVowels[x], indexVowels[x])
        )

        ordered = []
        for v in sortedVowels:
            ordered.extend([v] * countVowels[v])

        res = list(s)
        idx = 0

        for i in range(len(res)):
            if res[i] in countVowels:
                res[i] = ordered[idx]
                idx += 1

        return "".join(res)
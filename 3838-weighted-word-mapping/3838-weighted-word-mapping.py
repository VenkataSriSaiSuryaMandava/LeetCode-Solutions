class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""

        for word in words:
            weight = 0

            for ch in word:
                weight += weights[ord(ch) - ord('a')]
            
            weight = weight % 26

            res += chr(ord('z') - weight)

        return res
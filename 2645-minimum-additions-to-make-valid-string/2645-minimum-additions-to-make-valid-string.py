class Solution:
    def addMinimum(self, word: str) -> int:
        blocks = 1

        for i in range(1, len(word)):
            if word[i] <= word[i - 1]:
                blocks += 1
        
        return blocks * 3 - len(word)
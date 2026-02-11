class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        letters = set(brokenLetters)

        for word in text.split():
            for ch in word:
                if ch in letters:
                    break
            else:
                res += 1
        return res
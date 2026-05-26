class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        capset = set()
        smallset = set()

        res = 0

        for ch in word:
            if ord('a') <= ord(ch) <= ord('z'):
                smallset.add(ord(ch) - ord('a'))
            else:
                capset.add(ord(ch) - ord('A'))

        for ch in smallset:
            if ch in capset:
                res += 1
        
        return res
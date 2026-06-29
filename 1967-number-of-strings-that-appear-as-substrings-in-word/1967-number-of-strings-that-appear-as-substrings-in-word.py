class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrings = set()
        res = 0

        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substrings.add(word[i : j])
        
        for pattern in patterns:
            if pattern in substrings:
                res += 1
        
        return res
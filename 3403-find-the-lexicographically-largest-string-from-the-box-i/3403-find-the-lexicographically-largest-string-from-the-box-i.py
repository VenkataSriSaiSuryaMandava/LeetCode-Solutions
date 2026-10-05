class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        max_length = n - (numFriends - 1)
        for i in range(n):
            res = max(res, word[i:i+max_length])
        return res
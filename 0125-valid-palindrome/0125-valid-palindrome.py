class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = []
        for ch in s:
            if ch.isalnum():
                newS.append(ch.lower())
        i,j=0,len(newS)-1
        while i<=j:
            if newS[i] != newS[j]:  return False
            i += 1
            j -= 1
        return True
        
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        substrings = []
        start = 0
        height = 0

        for i, ch in enumerate(s):
            if ch == "1":
                height += 1
            else:
                height -= 1
            
            if height == 0:
                inner = self.makeLargestSpecial(s[start + 1 : i])
                substrings.append('1' + inner + '0')
                start = i + 1
        
        substrings.sort(reverse = True)
        return "".join(substrings)

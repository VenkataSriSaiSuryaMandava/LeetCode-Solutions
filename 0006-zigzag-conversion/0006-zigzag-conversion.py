class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:    return s
        res = ['' for _ in range(numRows)]
        direction = True
        i = 0
        for ch in s:
            res[i] += ch
            if i == numRows-1:
                direction = False
            elif i == 0:
                direction = True
            if direction:
                i += 1
            else:
                i -= 1
        return ''.join(res)
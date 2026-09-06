class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:   return s
        i = 0
        res = [""] * numRows
        direction = True
        for ch in s:
            res[i] += ch
            if i == 0:
                direction = True
            elif i == numRows-1:
                direction = False
            if direction:
                i += 1
            else:
                i -= 1
        return ''.join(res)

        
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowLen = len(mat)
        colLen = len(mat[0])
        res = 0

        rows = [0] * rowLen
        cols = [0] * colLen

        for i in range(rowLen):
            for j in range(colLen):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(rowLen):
            for j in range(colLen):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    res += 1
        
        return res
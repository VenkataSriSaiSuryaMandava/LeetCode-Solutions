class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])

        r = 0
        c = 0

        going_up = True
        res = []

        while len(res) != rows * cols:
            if going_up:
                while r >= 0 and c < cols:
                    res.append(mat[r][c])

                    r -= 1
                    c += 1
                
                if c == cols:
                    c -= 1
                    r += 2
                else:
                    r += 1
                
                going_up = False
            else:
                while r < rows and c >= 0:
                    res.append(mat[r][c])

                    r += 1
                    c -= 1
                
                if r == rows:
                    r -= 1
                    c += 2
                else:
                    c += 1
                
                going_up = True
        
        return res
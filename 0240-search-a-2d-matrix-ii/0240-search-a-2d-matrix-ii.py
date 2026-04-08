class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        r = m - 1
        c = 0

        while r >=0 and c < n:
            if target > matrix[r][c]:
                c += 1
            elif target < matrix[r][c]:
                r -= 1
            else:
                return True
        
        return False
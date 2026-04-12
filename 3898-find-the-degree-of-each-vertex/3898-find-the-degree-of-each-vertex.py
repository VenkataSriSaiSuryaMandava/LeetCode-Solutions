class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        for row in matrix:
            count = 0
            for i in row:
                count += i

            res.append(count)

        return res
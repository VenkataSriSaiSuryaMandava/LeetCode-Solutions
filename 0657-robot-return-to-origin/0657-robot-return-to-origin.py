class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0, 0]

        for m in moves:
            a, b = pos
            if m == 'U':
                pos = [a - 1, b]
            elif m == "D":
                pos = [a + 1, b]
            elif m == "R":
                pos = [a, b + 1]
            elif m == "L":
                pos = [a, b - 1]
        
        return pos == [0, 0]
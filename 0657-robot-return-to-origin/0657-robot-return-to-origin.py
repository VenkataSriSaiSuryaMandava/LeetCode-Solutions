class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]

        for op in moves:
            a, b = pos

            if op == 'U':
                pos = [a - 1, b]
            elif op == 'D':
                pos = [a + 1, b]
            elif op == 'L':
                pos = [a, b - 1]
            elif op == 'R':
                pos = [a, b + 1]
        
        return pos == [0, 0]
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        obstacles = {tuple(o) for o in obstacles}
        res = 0
        d = 0

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                
                for i in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    
                    x = x + dx
                    y = y + dy
                
                res = max(res, x ** 2 + y ** 2)
        
        return res
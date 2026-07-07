class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        distances = [0, 0, 0, 0]

        for instruction in instructions:
            if instruction == 'G':
                distances[direction] += 1
            elif instruction == 'L':
                direction = (direction + 1) % 4
            elif instruction == 'R':
                direction = (direction + 3) % 4
        
        return (((distances[0] == distances[2]) and 
                (distances[1] == distances[3])) or
                direction != 0)
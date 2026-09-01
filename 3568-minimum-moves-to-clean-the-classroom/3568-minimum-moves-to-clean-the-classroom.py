from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_coords = []
        start = None
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))
                    
        num_litters = len(litter_coords)
        if num_litters == 0:
            return 0
            
        target_mask = (1 << num_litters) - 1
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        
        max_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        queue = deque([(start[0], start[1], 0, energy, 0)])
        max_energy[start[0]][start[1]][0] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
                
            if cur_energy <= 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    cell = classroom[nr][nc]
                    
                    if cell == 'R':
                        next_energy = energy
                        
                    next_mask = mask
                    if cell == 'L' and (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                        
                    if next_energy > max_energy[nr][nc][next_mask]:
                        max_energy[nr][nc][next_mask] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
                        
        return -1
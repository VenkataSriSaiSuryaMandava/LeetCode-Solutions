class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        farthest = 0

        while queue:
            i = queue.popleft()
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump + 1, len(s))

            for j in range(start, end):
                if s[j] == "0":
                    queue.append(j)

                    if j == len(s) - 1:
                        return True
            
            farthest = i + maxJump

        return False
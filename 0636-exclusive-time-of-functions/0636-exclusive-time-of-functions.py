class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        prev = 0

        for log in logs:
            i, op, cur = log.split(":")
            i = int(i)
            cur = int(cur)

            if op == "start":
                if stack:
                    prev_id = stack[-1]
                    res[prev_id] += cur - prev

                stack.append(i)
                prev = cur
            else:
                prev_id = stack.pop()
                res[prev_id] += cur - prev + 1
                prev = cur + 1
        
        return res

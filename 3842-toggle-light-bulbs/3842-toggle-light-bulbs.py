class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        state = [False] * 101

        for b in bulbs:
            if state[b]:
                state[b] = False
            else:
                state[b] = True

        res = []
        for i, s in enumerate(state):
            if s:
                res.append(i)

        return res
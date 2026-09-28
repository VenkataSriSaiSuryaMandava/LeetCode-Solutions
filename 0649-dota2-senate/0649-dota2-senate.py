class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = deque()
        dire = deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while dire and radiant:
            dire_turn = dire.popleft()
            radiant_turn = radiant.popleft()

            if dire_turn < radiant_turn:
                dire.append(dire_turn + n)
            else:
                radiant.append(radiant_turn + n)
        
        if dire:
            return "Dire"
        else:
            return "Radiant"
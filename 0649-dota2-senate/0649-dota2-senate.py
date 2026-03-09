class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        R = deque()
        D = deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            R_turn = R.popleft()
            D_turn = D.popleft()

            if R_turn < D_turn:
                R.append(R_turn + n)
            else:
                D.append(D_turn + n)
        
        if R:
            return "Radiant"
        else:
            return "Dire"
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cntA = defaultdict(int)
        cntB = defaultdict(int)

        res = []

        for a, b in zip(A, B):
            cntA[a] += 1
            cntB[b] += 1
            
            total = 0
            for num, cnt in cntA.items():
                total += min(cnt, cntB[num])
            
            res.append(total)
        
        return res
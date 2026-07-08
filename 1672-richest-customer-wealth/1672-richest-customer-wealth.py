class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0

        for account in accounts:
            total = 0

            for money in account:
                total += money
            
            res = max(res, total)
        
        return res
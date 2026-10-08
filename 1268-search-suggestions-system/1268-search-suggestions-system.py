class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        res = []
        products.sort()

        l = 0 
        r = len(products) - 1

        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1
            
            res.append([])
            remain = min(r - l + 1, 3)

            for j in range(remain):
                res[-1].append(products[l + j])
        
        return res
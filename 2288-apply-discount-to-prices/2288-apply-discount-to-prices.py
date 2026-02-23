class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = []
        words = sentence.split(" ")

        for word in words:
            if word[0] == "$" and word[1 : ].isdigit():
                price = int(word[1 : ])
                discounted = price * (100 - discount) / 100
                res.append(f"${discounted:.2f}")
            else:
                res.append(word)
        
        return " ".join(res)
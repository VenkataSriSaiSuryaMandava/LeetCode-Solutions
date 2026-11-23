class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefix = [1]

    def add(self, num: int) -> None:
        self.stream.append(num)

        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.prefix) <= k:
            return 0
        else:
            return self.prefix[-1] // self.prefix[- k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
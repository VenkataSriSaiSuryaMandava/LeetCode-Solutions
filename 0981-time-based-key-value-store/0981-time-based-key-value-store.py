class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.timestamps[key]) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2

            if self.timestamps[key][m][1] <= timestamp:
                res = self.timestamps[key][m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
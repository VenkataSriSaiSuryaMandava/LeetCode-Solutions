class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timestamps[key]

        l = 0 
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if timestamp <= arr[m][1]:
                r = m - 1
            else:
                l = m + 1
        
        return arr[m][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
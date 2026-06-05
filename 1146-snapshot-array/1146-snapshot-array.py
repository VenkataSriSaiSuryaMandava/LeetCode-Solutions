class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for i in range(length)]
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.i, val))

    def snap(self) -> int:
        self.i += 1
        return self.i - 1
        
    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_left(self.arr[index], (snap_id, inf)) - 1

        if idx < 0:
            return 0
        
        return self.arr[index][idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
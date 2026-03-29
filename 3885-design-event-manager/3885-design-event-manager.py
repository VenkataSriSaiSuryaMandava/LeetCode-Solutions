class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = []
        self.cur = {}

        for eventId, priority in events:
            self.cur[eventId] = priority
            heapq.heappush(self.heap, (-priority, eventId))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.cur[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            priority, eventId = heapq.heappop(self.heap)
            priority = priority * -1

            if eventId in self.cur and self.cur[eventId] == priority:
                del self.cur[eventId]
                return eventId

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
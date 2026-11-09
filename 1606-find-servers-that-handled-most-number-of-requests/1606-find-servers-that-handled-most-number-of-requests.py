class Solution:

  def busiestServers(
      self, k: int, arrival: list[int], load: list[int]
  ) -> list[int]:
    available = SortedList(range(k))
    busy = []
    count = [0] * k

    for i, (t, l) in enumerate(zip(arrival, load)):
      while busy and busy[0][0] <= t:
        _, server_id = heapq.heappop(busy)
        available.add(server_id)

      if not available:
        continue

      idx = available.bisect_left(i % k)
      if idx == len(available):
        idx = 0

      server_id = available.pop(idx)
      heapq.heappush(busy, (t + l, server_id))
      count[server_id] += 1

    max_handled = max(count)
    return [server for server, cnt in enumerate(count) if cnt == max_handled]